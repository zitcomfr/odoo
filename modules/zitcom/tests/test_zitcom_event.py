from openerp.tests.common import TransactionCase


class ZitcomEventCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(ZitcomEventCase, self).setUp(*args, **kwargs)
        self.event1 = self.env['zitcom.event'].create(
            {'name': "test", 'date': '2016-12-25'}
        )
        self.event2 = self.env['zitcom.event'].create(
            {'name': "test 2", 'date':'2017-02-01'}
        )


    def tearDown(self, *args, **kwargs):
        return super(ZitcomEventCase, self).tearDown(*args, **kwargs)

    def test_coteup(self):
        self.assertEqual(
            "up",
            self.event2.cote
        )

    def test_cotedown(self):
        self.assertEqual(
            "down",
            self.event1.cote
        )
