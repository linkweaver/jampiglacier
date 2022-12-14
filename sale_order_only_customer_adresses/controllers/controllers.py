# -*- coding: utf-8 -*-
# from odoo import http


# class ClientStatAnalysis(http.Controller):
#     @http.route('/client_stat_analysis/client_stat_analysis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/client_stat_analysis/client_stat_analysis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('client_stat_analysis.listing', {
#             'root': '/client_stat_analysis/client_stat_analysis',
#             'objects': http.request.env['client_stat_analysis.client_stat_analysis'].search([]),
#         })

#     @http.route('/client_stat_analysis/client_stat_analysis/objects/<model("client_stat_analysis.client_stat_analysis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('client_stat_analysis.object', {
#             'object': obj
#         })
