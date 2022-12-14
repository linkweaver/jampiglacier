from odoo import models, fields, api

LOCKED_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'done', 'cancel'}
}

class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string="Invoice Address",
        compute='_compute_partner_invoice_id',
        store=True, readonly=False, required=True, precompute=True,
        states=LOCKED_FIELD_STATES,
        domain="['|', ('parent_id','=',partner_id), ('id','=',partner_id)]")
        #old domin is here
        #domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    partner_shipping_id = fields.Many2one(
        comodel_name='res.partner',
        string="Delivery Address",
        compute='_compute_partner_shipping_id',
        store=True, readonly=False, required=True, precompute=True,
        states=LOCKED_FIELD_STATES,
        domain="['|', ('parent_id','=',partner_id), ('id','=',partner_id)]")
        #old domin is here
        #domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)