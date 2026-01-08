{
    "name": "Nigerian Address Integration",
    "version": "18.0.1.0.0",
    "category": "Localization",
    "summary": "Integrate the Nigerian addressing system (States and LGAs) into Odoo.",
    "author": "Babatope Ajepe",
    "website": "https://www.google.com",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_country_state_data.xml",
        "data/res.country.lga.csv",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
