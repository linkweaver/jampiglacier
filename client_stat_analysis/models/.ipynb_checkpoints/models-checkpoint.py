# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class client_stat_analysis(models.Model):
#     _name = 'client_stat_analysis.client_stat_analysis'
#     _description = 'client_stat_analysis.client_stat_analysis'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
