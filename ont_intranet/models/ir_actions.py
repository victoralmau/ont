# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class IrActionsActUrl(models.Model):
    _inherit = 'ir.actions.act_url'

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        res_items = super(IrActionsActUrl, self).read(fields, load=load)
        if load == '_classic_read':
            res_items = super(IrActionsActUrl, self).read(fields, load=load)
            key = 0
            for res_item in res_items:
                if "intranet." in res_item['url']:
                    if "?" in res_item['url']:
                        res_items[key]['url'] = "%s&odoo_password_crypt=%s" % (
                            res_item['url'],
                            self.env.user.password_crypt
                        )
                    else:
                        res_items[key]['url'] = "%s?odoo_password_crypt=%s" % (
                            res_item['url'],
                            self.env.user.password_crypt
                        )

                key = key + 1

        return res_items
