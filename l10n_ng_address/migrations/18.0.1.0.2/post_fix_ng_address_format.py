from odoo import SUPERUSER_ID, api

ADDRESS_FORMAT = (
    "%(street)s\n%(street2)s\n%(city)s\n%(lga_name)s\n"
    "%(state_name)s\n%(zip)s\n%(country_name)s"
)


def migrate(cr, version):
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})
    nigeria = env.ref("base.ng", raise_if_not_found=False)
    if not nigeria or not nigeria.address_format:
        return

    # Only rewrite the known-broken format set by earlier releases, so a
    # user-customized address format is left untouched.
    if "%(state_id)s" in nigeria.address_format or "%(country_id)s" in nigeria.address_format:
        nigeria.write({"address_format": ADDRESS_FORMAT})
