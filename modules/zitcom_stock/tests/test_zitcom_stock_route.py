from odoo.tests.common import TransactionCase


class ZitcomRouteCase(TransactionCase):

    def setUp(self):
        super(ZitcomRouteCase, self).setUp()
        self.test_order = self.env.ref('zitcom_stock.sale_order_le_mag')

    def test_dispatched_sale_order(self):
        # minimalist test, while validating sale_order_le_mag
        # that should create 3 stock.pickngs
        self.test_order.action_confirm()
        self.assertEqual(
            len(self.test_order.picking_ids),
            3
        )
