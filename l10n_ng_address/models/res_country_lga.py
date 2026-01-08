from odoo import fields, models


class ResCountryLga(models.Model):
    _name = "res.country.lga"
    _description = "Local Government Area"
    _order = "name"

    name = fields.Char(string="LGA Name", required=True)
    state_id = fields.Many2one(
        "res.country.state",
        string="State",
        required=True,
        domain="[('country_id.code', '=', 'NG')]",
    )
