from odoo import api, fields, models


class ResCountryLga(models.Model):
    _name = "res.country.lga"
    _description = "Local Government Area"
    _order = "state_id, name"
    _sql_constraints = [
        (
            "name_state_uniq",
            "unique(state_id, name)",
            "An LGA with this name already exists in the selected state.",
        ),
    ]

    name = fields.Char(string="LGA Name", required=True)
    state_id = fields.Many2one(
        "res.country.state",
        string="State",
        required=True,
        domain="[('country_id.code', '=', 'NG')]",
    )

    @api.depends("name", "state_id.name")
    def _compute_display_name(self):
        for lga in self:
            if lga.state_id:
                lga.display_name = f"{lga.name} ({lga.state_id.name})"
            else:
                lga.display_name = lga.name
