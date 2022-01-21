# -*- coding: utf-8 -*-
#
# Copyright 2019 Luxim d.o.o., Slovenia <https://luxim.si>
# Author: Matjaž Mozetič <matjaz@luxim.si>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import date
from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    date_invoice_creation = fields.Date(
        string='Issue Date',
        readonly=True,
        states={'draft': [('readonly', False)]},
        index=True,
        default=lambda *a: date.today().strftime('%Y-%m-%d'),
        help="Date when invoice was issued."
    )

    date_invoice = fields.Date(
        string='Service Date',
        required=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        index=True,
        default=lambda *a: date.today().strftime('%Y-%m-%d'),
        help="Date when debt relationship between customer "
             "and supplier started."
    )

    date_invoice_received = fields.Date(
        string='Date Received',
        readonly=True,
        states={'draft': [('readonly', False)]},
        index=True,
        default=lambda *a: date.today().strftime('%Y-%m-%d'),
        help="Date when supplier invoice was received."
    )

    @api.multi
    def action_date_assign(self):
        for inv in self:
            if not inv.date_due:
                super(AccountInvoice, self).action_date_assign()
        return True
