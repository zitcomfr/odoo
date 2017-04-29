# -*- coding: utf-8 -*-
from odoo import models


class StockMove(models.Model):

    _inherit = 'stock.move'

    def _push_apply(self):
        # PV: Overwrite _push_apply to handle push route defined on sale
        #  order line.
        Push = self.env['stock.location.path']
        for move in self:
            # if the move is already chained, there is no need to check push
            # rules
            if move.move_dest_id:
                continue
            # if the move is a returned move, we don't want to check push
            # rules, as returning a returned move is the only decent way
            # to receive goods without triggering the push rules again
            # (which would duplicate chained operations)
            domain = [('location_from_id', '=', move.location_dest_id.id)]
            # priority goes to the route defined on the product and
            # product category
            routes = move.product_id.route_ids | move.product_id.categ_id.\
                total_route_ids
            # PV: START CHANGE
            # add route defined on sale order lines
            if (
                move.procurement_id and move.procurement_id.sale_line_id and
                move.procurement_id.sale_line_id.route_id
            ):
                routes |= move.procurement_id.sale_line_id.route_id
            # PV: END CHANGE

            rules = Push.search(
                domain + [('route_id', 'in', routes.ids)],
                order='route_sequence, sequence',
                limit=1
            )
            if not rules:
                # TDE FIXME/ should those really be in a if / elif ??
                # then we search on the warehouse if a rule can apply
                if move.warehouse_id:
                    rules = Push.search(
                        domain + [
                            ('route_id', 'in', move.warehouse_id.route_ids.ids)
                        ],
                        order='route_sequence, sequence',
                        limit=1
                    )
                elif move.picking_id.picking_type_id.warehouse_id:
                    rules = Push.search(
                        domain + [
                            (
                                'route_id',
                                'in',
                                move.picking_id.picking_type_id.warehouse_id.
                                route_ids.ids
                            )
                        ],
                        order='route_sequence, sequence',
                        limit=1
                    )
            if not rules:
                # if no specialized push rule has been found yet,
                # we try to find a general one (without route)
                rules = Push.search(
                    domain + [('route_id', '=', False)],
                    order='sequence',
                    limit=1
                )
            # Make sure it is not returning the return
            if (
                rules and (
                    not move.origin_returned_move_id or
                    move.origin_returned_move_id.location_dest_id.id !=
                    rules.location_dest_id.id
                )
            ):
                rules._apply(move)
        return True
