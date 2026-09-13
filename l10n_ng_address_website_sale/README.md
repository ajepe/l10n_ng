# Nigerian Address Integration - eCommerce

Adds the Nigerian Local Government Area (LGA) to the eCommerce checkout
address form and to the address pages under `/shop/address`, and saves it
on the contact.

The module requires `l10n_ng_address` and `website_sale` and is installed
automatically when both are present.

## How it works

- The checkout address form gets an LGA select under the State field. The
  field is only shown when the selected country is Nigeria.
- The options are filtered by the selected state. Changing the country or
  the state clears the selection.
- `lga_id` is whitelisted for the checkout form so the value is written on
  the partner when the address is saved.
- If the posted LGA does not belong to the selected state, the form shows
  an error and does not save it.
- The address format from `l10n_ng_address` already prints the LGA on the
  checkout address cards, orders and invoices.

## Tests

    odoo-bin -d <database> -i l10n_ng_address_website_sale --test-enable --stop-after-init
