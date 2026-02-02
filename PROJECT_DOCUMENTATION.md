# Nigeria Localization (l10n_ng)

## Overview

This project provides Nigerian localization for Odoo 18.0, specifically focusing on integrating the Nigerian addressing system into the ERP platform.

## Module Structure

### l10n_ng_address

The main module that handles Nigerian address integration with the following components:

**Core Features:**
- **LGA Model**: Introduces `res.country.lga` model to store Nigeria's 774 Local Government Areas
- **Enhanced Contact Forms**: Adds LGA field to partner/contact forms with state-based filtering
- **Complete Data**: Includes all 36 Nigerian states plus FCT and their corresponding LGAs
- **Address Formatting**: Updates Nigerian address format to include LGA in documents

**Technical Implementation:**
- `res_country_lga.py`: LGA model with state relationship
- `res_partner.py`: Partner model extension with LGA field and address formatting
- `res_country_state_data.xml`: Nigerian states data
- `res.country.lga.csv`: Complete LGA data import
- `res_partner_views.xml`: Updated contact form views

## Installation

1. Copy `l10n_ng_address` directory to Odoo addons folder
2. Restart Odoo server
3. Install module via Apps menu (search "Nigerian Address Integration")

## Usage

1. Navigate to Contacts module
2. Select Nigeria as country
3. Choose State from dropdown
4. LGA field auto-filters based on selected state
5. LGA appears in formatted addresses on documents

## Author & License

- Author: Babatope Ajepe
- License: LGPL-3
- Version: 18.0.1.0.0
- Website: https://www.google.com