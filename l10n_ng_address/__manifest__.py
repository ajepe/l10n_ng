{
    "name": "Nigerian Address Integration",
    "version": "18.0.1.0.2",
    "category": "Localization",
    "summary": "Integrate the Nigerian addressing system (States and LGAs) into Odoo.",
    "author": "Babatope Ajepe",
    "website": "https://github.com/ajepe/l10n_ng",
    "countries": ["ng"],
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_country_data.xml",
        "data/res_country_state_data.xml",
        "data/res.country.lga.csv",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
