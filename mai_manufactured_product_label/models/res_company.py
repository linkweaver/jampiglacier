# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class Company(models.Model):
    _inherit = "res.company"

    hrn = fields.Char(string="HRN")
    datas = fields.Binary(string="Company Logo")
    datas_fname = fields.Char('File Name')