import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})
    duplicate = env.ref(
        "l10n_ng_address.lga_os_ile_ogbo", raise_if_not_found=False
    )
    if not duplicate:
        return

    ila = env.ref("l10n_ng_address.lga_os_ila", raise_if_not_found=False)
    partners = env["res.partner"].search([("lga_id", "=", duplicate.id)])
    if partners:
        partners.write({"lga_id": ila.id if ila else False})
        _logger.info(
            "l10n_ng_address: reassigned %s partner(s) from Ila-Orangun to Ila",
            len(partners),
        )
    duplicate.unlink()
    _logger.info("l10n_ng_address: removed duplicate Ila-Orangun LGA")
