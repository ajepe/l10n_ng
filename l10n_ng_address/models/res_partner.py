from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    lga_id = fields.Many2one(
        "res.country.lga",
        string="LGA",
        domain="[ ('state_id', '=', state_id)]",
    )
    lga_name = fields.Char(string="LGA Name", related="lga_id.name")

    @api.onchange("state_id")
    def _onchange_state_id(self):
        """
        When the state is changed, clear the LGA field.
        """
        if self.state_id != self.lga_id.state_id:
            self.lga_id = False

    @api.model
    def _formatting_address_fields(self):
        return super()._formatting_address_fields() + ["lga_name"]
