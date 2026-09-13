
# -*- coding: utf-8 -*-

from odoo.tests.common import Form, TransactionCase


class TestNigerianAddress(TransactionCase):
    """
    Tests for the Nigerian Address module.
    """

    def setUp(self, *args, **kwargs):
        super(TestNigerianAddress, self).setUp(*args, **kwargs)
        self.Partner = self.env["res.partner"]
        self.State = self.env["res.country.state"]
        self.Lga = self.env["res.country.lga"]
        self.nigeria = self.env.ref("base.ng")

    def test_01_data_loading(self):
        """Test that the Nigerian states and LGAs are loaded correctly."""
        # Check if a few key states are loaded
        lagos_state = self.State.search([("code", "=", "LA"), ("country_id", "=", self.nigeria.id)])
        self.assertTrue(lagos_state, "Lagos state not found.")

        abuja_state = self.State.search([("code", "=", "FC"), ("country_id", "=", self.nigeria.id)])
        self.assertTrue(abuja_state, "FCT (Abuja) not found.")

        # Check if a few key LGAs are loaded
        ikeja_lga = self.Lga.search([("name", "=", "Ikeja"), ("state_id", "=", lagos_state.id)])
        self.assertTrue(ikeja_lga, "Ikeja LGA not found.")

        abuja_municipal_lga = self.Lga.search([("name", "=", "Abuja Municipal Area Council"), ("state_id", "=", abuja_state.id)])
        self.assertTrue(abuja_municipal_lga, "Abuja Municipal Area Council LGA not found.")

        # The dataset must contain the 774 official LGAs
        lga_count = self.Lga.search_count([("state_id.country_id", "=", self.nigeria.id)])
        self.assertEqual(lga_count, 774, "Expected 774 LGAs, found %s." % lga_count)

    def test_02_onchange_state_id(self):
        """Test the onchange method for the state_id field."""
        lagos_state = self.State.search([("code", "=", "LA"), ("country_id", "=", self.nigeria.id)])
        ikeja_lga = self.Lga.search([("name", "=", "Ikeja"), ("state_id", "=", lagos_state.id)])

        partner = self.Partner.create({
            "name": "Test Partner",
            "country_id": self.nigeria.id,
            "state_id": lagos_state.id,
            "lga_id": ikeja_lga.id,
        })

        # Change the state through a form and check if the LGA is cleared
        rivers_state = self.State.search([("code", "=", "RI"), ("country_id", "=", self.nigeria.id)])
        with Form(partner) as partner_form:
            partner_form.state_id = rivers_state
            self.assertFalse(partner_form.lga_id, "LGA should be cleared when the state is changed.")

    def test_03_address_format(self):
        """Test that the address format for Nigeria includes the LGA."""
        lagos_state = self.State.search([("code", "=", "LA"), ("country_id", "=", self.nigeria.id)])
        ikeja_lga = self.Lga.search([("name", "=", "Ikeja"), ("state_id", "=", lagos_state.id)])

        partner = self.Partner.create({
            "name": "Test Partner",
            "street": "123 Main Street",
            "city": "Ikeja",
            "country_id": self.nigeria.id,
            "state_id": lagos_state.id,
            "lga_id": ikeja_lga.id,
        })

        address = partner._display_address(without_company=True)
        self.assertEqual(
            address,
            "123 Main Street\n\nIkeja\nIkeja\nLagos\n\nNigeria",
            "Unexpected Nigerian address format: %r" % address,
        )
