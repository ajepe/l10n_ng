{
    "name": "Nigerian Address Integration - eCommerce",
    "version": "18.0.1.0.0",
    "category": "Localization",
    "summary": "Show the Nigerian LGA in the eCommerce checkout address form.",
    "author": "Babatope Ajepe",
    "website": "https://github.com/ajepe/l10n_ng",
    "countries": ["ng"],
    "depends": ["l10n_ng_address", "website_sale"],
    "data": [
        "data/ir_model_fields.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "l10n_ng_address_website_sale/static/src/js/website_sale.js",
        ],
    },
    "auto_install": True,
    "installable": True,
    "license": "LGPL-3",
}
