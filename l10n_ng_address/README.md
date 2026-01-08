
# Nigerian Address Integration

## Overview

This module integrates the Nigerian addressing system into Odoo 18.0. It addresses the gaps in the default Odoo installation by providing a structured way to handle Nigerian addresses, including States and Local Government Areas (LGAs).

This module was created by Gemini.

## Features

*   **LGA Model:** Adds a new model (`res.country.lga`) to store the list of all 774 Nigerian Local Government Areas.
*   **Partner Form Update:** Adds a new "LGA" field to the contact form, which is dynamically filtered based on the selected state.
*   **Comprehensive Data:** Includes a complete and up-to-date list of all 36 Nigerian states (plus the FCT) and their corresponding 774 LGAs.
*   **Address Formatting:** Updates the address format for Nigeria to include the LGA, ensuring it appears on all documents, such as invoices and delivery orders.

## Installation

To install this module, you need to:

1.  **Copy the `l10n_ng_address` directory** to the `addons` folder of your Odoo 18.0 installation.
2.  **Restart the Odoo server.**
3.  **Go to the "Apps" menu** in Odoo, remove the "Apps" filter, and search for "Nigerian Address Integration".
4.  **Click "Install"** to install the module.

## Usage

Once the module is installed, you can use the new addressing system as follows:

1.  Go to the **Contacts** module and open or create a new contact.
2.  When you select **Nigeria** as the country, you will see the **State** and **LGA** fields.
3.  Select a **State** from the dropdown list.
4.  The **LGA** field will then be automatically filtered to show only the LGAs belonging to the selected state.
5.  When you save the address, the LGA will be included in the formatted address.

This module provides a seamless and user-friendly way to handle Nigerian addresses in Odoo.
