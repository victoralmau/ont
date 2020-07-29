# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
        
    margin = fields.Float(
        string='Margin'
    )
    margin_percent = fields.Float(
        string='Margin %'
    )
    
    @api.one
    def action_calculate_margin_percent(self):
        self.margin_percent = 0
        if self.margin != 0 and self.price_subtotal > 0:
            margin_line_percent = (self.margin / self.price_subtotal) * 100
            self.margin_percent = "{:.2f}".format(margin_line_percent)
