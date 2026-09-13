from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleL10nNgAddress(WebsiteSale):

    def _prepare_address_form_values(
        self,
        order_sudo,
        partner_sudo,
        address_type,
        use_delivery_as_billing,
        callback="",
        **kwargs,
    ):
        values = super()._prepare_address_form_values(
            order_sudo,
            partner_sudo,
            address_type,
            use_delivery_as_billing,
            callback=callback,
            **kwargs,
        )
        country = values["country"]
        state = partner_sudo.state_id
        if country and country.code == "NG" and state:
            lgas = (
                request.env["res.country.lga"]
                .sudo()
                .search([("state_id", "=", state.id)], order="name")
            )
        else:
            lgas = request.env["res.country.lga"].sudo().browse()
        values["lgas"] = lgas
        values["lga_id"] = partner_sudo.lga_id.id
        return values

    def _validate_address_values(
        self,
        address_values,
        partner_sudo,
        address_type,
        use_delivery_as_billing=None,
        required_fields=None,
        is_main_address=True,
        **kwargs,
    ):
        invalid_fields, missing_fields, error_messages = super()._validate_address_values(
            address_values,
            partner_sudo,
            address_type,
            use_delivery_as_billing,
            required_fields,
            is_main_address=is_main_address,
            **kwargs,
        )

        lga_id = address_values.get("lga_id")
        if lga_id:
            lga = request.env["res.country.lga"].sudo().browse(lga_id)
            if lga.state_id.id != address_values.get("state_id"):
                invalid_fields.add("lga_id")
                error_messages.append(
                    request.env._(
                        "The selected Local Government Area does not belong to the"
                        " selected state."
                    )
                )
        return invalid_fields, missing_fields, error_messages


class L10nNgAddressWebsiteSale(http.Controller):

    @http.route(
        "/shop/lga_infos/<model('res.country.state'):state>",
        type="json",
        auth="public",
        methods=["POST"],
        website=True,
    )
    def lga_infos(self, state, **kwargs):
        lgas = (
            request.env["res.country.lga"]
            .sudo()
            .search([("state_id", "=", state.id)], order="name")
        )
        return {"lgas": [(lga.id, lga.name) for lga in lgas]}
