from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = "sale.report"

    #Attention à reprendre les données qui sont directement à partir du champ de relation
    x_famille_client_id = fields.Many2one('x_famille_client', string='Famille client', readonly=True)
    x_detail_client_id = fields.Many2one('x_detail_client', string='Détail client', readonly=True)
    x_canal_general_client_id = fields.Many2one('x_canal_general_client', string='Canal général client', readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['x_famille_client_id'] = "partner.x_studio_famille"
        res['x_canal_general_client_id'] = "partner.x_studio_canal_general"
        res['x_detail_client_id'] = "partner.x_studio_detail_client"
        
        return res 
    
    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            partner.x_studio_famille,
            partner.x_studio_canal_general,
            partner.x_studio_detail_client
            """
        return res