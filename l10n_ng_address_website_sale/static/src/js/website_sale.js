/** @odoo-module **/

import websiteSaleAddress from "@website_sale/js/address";
import { rpc } from "@web/core/network/rpc";

websiteSaleAddress.include({
    start: function () {
        this._super.apply(this, arguments);
        this.elementLga = this.addressForm && this.addressForm.lga_id;
        this.elementLgaDiv = document.getElementById("div_lga");
    },

    _selectedCountryCode: function () {
        const select = this.addressForm.country_id;
        if (!select || !select.value || !select.selectedOptions.length) {
            return "";
        }
        return select.selectedOptions[0].getAttribute("code") || "";
    },

    _changeLgaOptions: function (choices) {
        const select = this.elementLga;
        if (!select) {
            return;
        }
        // Keep the placeholder option.
        select.options.length = 1;
        choices.forEach((lga) => {
            select.appendChild(new Option(lga[1], lga[0]));
        });
        if (this.elementLgaDiv) {
            this.elementLgaDiv.style.display = choices.length ? "" : "none";
        }
    },

    _onChangeState: async function () {
        await this._super(...arguments);
        if (!this.elementLga) {
            return;
        }
        let choices = [];
        if (this._selectedCountryCode() === "NG" && this.addressForm.state_id.value) {
            const data = await rpc(
                `/shop/lga_infos/${parseInt(this.addressForm.state_id.value)}`,
                {}
            );
            choices = data.lgas;
        }
        this._changeLgaOptions(choices);
    },

    _changeCountry: async function (init = false) {
        await this._super(...arguments);
        if (!this.elementLga || init) {
            return;
        }
        if (this._selectedCountryCode() !== "NG") {
            this._changeLgaOptions([]);
        }
    },
});
