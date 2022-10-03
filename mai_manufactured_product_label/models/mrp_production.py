# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # @api.multi
    def print_product_label(self):
        return self.env.ref('mai_manufactured_product_label.action_report_product_label').report_action(self)

    # @api.multi
    def get_expiry_date(self):
        expitry = ''
        if self.product_id and self.product_id.removal_time and self.date_finished:
            expitry = datetime.strptime(str(self.date_finished), DEFAULT_SERVER_DATETIME_FORMAT).date() + timedelta(days=self.product_id.removal_time)
            expitry = expitry.strftime("%d-%m-%Y")
        return expitry

    # @api.multi
    def get_product_bom_components(self):
        bom_products = ''
        if self.product_id and self.bom_id and self.bom_id.bom_line_ids:
            bom_products = ', '.join([product.product_id.name for product in self.bom_id.bom_line_ids])
        return bom_products