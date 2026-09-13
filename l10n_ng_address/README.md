# Nigerian Address Integration

Adds Nigeria's states and Local Government Areas (LGAs) to contacts and
includes the LGA in Nigerian addresses printed on documents.

This module only handles addresses. Odoo's accounting localization for
Nigeria is a separate module (`l10n_ng`).

- Odoo version: 18.0
- Dependencies: `base`, `contacts`
- License: LGPL-3

## Installation

1. Put the `l10n_ng_address` directory in one of the addons paths of your
   Odoo installation.
2. Restart the Odoo service.
3. In the Apps menu, clear the "Apps" filter, search for "Nigerian Address
   Integration" and click Install.

## How it works

### LGA data

The module provides the 36 states, the Federal Capital Territory and the
774 LGAs. States are defined in `data/res_country_state_data.xml` and LGAs
in `data/res.country.lga.csv`.

LGAs are stored in a new model, `res.country.lga`, with two fields: `name`
and `state_id` (required). A name can only appear once per state, and
records are shown as `Ikeja (Lagos)` in the dropdowns.

State records are loaded as "no update" data, so renaming a state in the
database is not undone by a module upgrade. LGA records are loaded from the
CSV file and refreshed on every upgrade, which means edits to the LGAs that
come from the file are lost. Custom entries should be added as new records.

### Contacts

The module adds an `lga_id` field to partners and displays it below the
State field on the contact form and in the address popup. The list only
shows LGAs of the selected state, and the LGA is cleared when the state
changes. Creating an LGA from the field is disabled, since the list is
reference data.

On the eCommerce checkout, the LGA field is provided by the companion
module `l10n_ng_address_website_sale`.

### Address format

The Nigerian address format is set to:

    street
    street2
    city
    LGA
    state
    postal code
    country

The format reads the related `lga_name` field of the partner, so no extra
input is needed. The LGA therefore appears on every document that prints a
partner address, such as invoices, delivery orders and portal pages.

## Permissions

Internal, portal and public users can read LGAs, because the address format
uses them. There is no menu to manage LGAs; the provided list normally does
not need to be edited.

## Tests

    odoo-bin -d <database> -i l10n_ng_address --test-enable --stop-after-init

## Uninstall

Uninstalling deletes the states and LGAs that come with the module and
removes the LGA field from contacts. The Nigerian address format stays in
the database and is not reverted automatically.
