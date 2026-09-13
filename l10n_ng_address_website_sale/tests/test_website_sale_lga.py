from odoo.tests import tagged

from odoo.addons.base.tests.common import BaseUsersCommon
from odoo.addons.website.tools import MockRequest
from odoo.addons.website_sale.tests.common import WebsiteSaleCommon

from odoo.addons.l10n_ng_address_website_sale.controllers.main import (
    L10nNgAddressWebsiteSale,
    WebsiteSaleL10nNgAddress,
)


@tagged("post_install", "-at_install")
class TestWebsiteSaleLga(BaseUsersCommon, WebsiteSaleCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.nigeria = cls.env.ref("base.ng")
        cls.lagos = cls.env.ref("l10n_ng_address.state_lagos")
        cls.rivers = cls.env.ref("l10n_ng_address.state_rivers")
        cls.ikeja = (
            cls.env["res.country.lga"]
            .search([("name", "=", "Ikeja"), ("state_id", "=", cls.lagos.id)], limit=1)
        )
        cls.port_harcourt = (
            cls.env["res.country.lga"]
            .search(
                [("name", "=", "Port Harcourt"), ("state_id", "=", cls.rivers.id)],
                limit=1,
            )
        )
        cls.WebsiteSaleController = WebsiteSaleL10nNgAddress()
        cls.LgaController = L10nNgAddressWebsiteSale()

    def _create_nigerian_partner(self, **values):
        return self.env["res.partner"].create(dict({
            "name": "Nigerian Customer",
            "street": "12 Marina Road",
            "city": "Lagos",
            "phone": "+2348000000000",
            "country_id": self.nigeria.id,
            "state_id": self.lagos.id,
            "lga_id": self.ikeja.id,
        }, **values))

    def _validate(self, partner, address_values):
        order = self._create_so(partner_id=partner.id)
        with MockRequest(self.env, website=self.website, sale_order_id=order.id):
            return self.WebsiteSaleController._validate_address_values(
                address_values, partner, "billing", False, "", True,
            )

    def _address_values(self, partner, **values):
        return dict({
            "name": partner.name,
            "email": "customer@example.com",
            "street": partner.street,
            "city": partner.city,
            "zip": "100001",
            "phone": partner.phone,
            "country_id": self.nigeria.id,
            "state_id": self.lagos.id,
            "lga_id": self.ikeja.id,
        }, **values)

    def test_01_prepare_address_form_values(self):
        partner = self._create_nigerian_partner()
        order = self._create_so(partner_id=partner.id)
        with MockRequest(self.env, website=self.website, sale_order_id=order.id):
            values = self.WebsiteSaleController._prepare_address_form_values(
                order,
                partner,
                address_type="billing",
                use_delivery_as_billing=False,
            )
        self.assertEqual(values["lga_id"], self.ikeja.id)
        self.assertIn(self.ikeja, values["lgas"])
        self.assertNotIn(self.port_harcourt, values["lgas"])

    def test_02_prepare_address_form_values_other_country(self):
        partner = self.env["res.partner"].create({
            "name": "US Customer",
            "country_id": self.country_us.id,
            "state_id": self.country_us_state_id,
        })
        order = self._create_so(partner_id=partner.id)
        with MockRequest(self.env, website=self.website, sale_order_id=order.id):
            values = self.WebsiteSaleController._prepare_address_form_values(
                order,
                partner,
                address_type="billing",
                use_delivery_as_billing=False,
            )
        self.assertFalse(values["lga_id"])
        self.assertFalse(values["lgas"])

    def test_03_validate_lga_from_another_state(self):
        partner = self._create_nigerian_partner()
        invalid_fields, _missing_fields, error_messages = self._validate(
            partner,
            self._address_values(partner, state_id=self.rivers.id),
        )
        self.assertIn("lga_id", invalid_fields)
        self.assertTrue(error_messages)

    def test_04_validate_lga_from_the_selected_state(self):
        partner = self._create_nigerian_partner()
        invalid_fields, _missing_fields, error_messages = self._validate(
            partner,
            self._address_values(partner),
        )
        self.assertNotIn("lga_id", invalid_fields)
        self.assertFalse(error_messages)

    def test_05_lga_infos_route(self):
        with MockRequest(self.env, website=self.website):
            result = self.LgaController.lga_infos(self.lagos)
        names = [name for _id, name in result["lgas"]]
        self.assertIn("Ikeja", names)
        self.assertNotIn("Port Harcourt", names)
