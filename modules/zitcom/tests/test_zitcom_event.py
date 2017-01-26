from openerp.tests.common import TransactionCase

class ZitcomEventCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(ZitcomEventCase, self).setUp(*args, **kwargs)
	

    def tearDown(self, *args, **kwargs):
        return super(ZitcomEventCase, self).tearDown(*args, **kwargs)

    def test_coteup(self):
        """First line of docstring appears in test logs.
        Other lines do not.
        Any method starting with ``test_`` will be tested.
        """
        pass

