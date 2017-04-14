# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class ZitcomEvent(models.Model):
    _name = "zitcom.event"

    # Attribut name sur chaque objet d'Odoo
    # https://www.odoo.com/documentation/10.0/reference/orm.html#fields
    name = fields.Char("title", required=True)
    date = fields.Date("date")
    lieu = fields.Many2one('zitcom.lieu', 'Lieu')
    cote = fields.Selection(
        selection=[
            ("up", u"Évènement ayant la côte"),
            ("equal", u"Tendance égale"),
            ("down", u"Côte descendante"),
        ],
        string="Côte de popularité",
        compute="get_cote",

    )

    @api.depends('date')
    def get_cote(self):
        for record in self:
            if record.date < '2016-12-31':
                record.cote = "down"
            else:
                record.cote = "up"


class ZitcomLieu(models.Model):
    _name = "zitcom.lieu"
    name = fields.Char("name", required=True)
    # geo_point = fields.GeoPoint('Addresses coordinate')
