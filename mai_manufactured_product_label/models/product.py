# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    energetic_ids = fields.One2many('energetic.value', 'template_id', string="Energetic values")
    allergy_image_ids = fields.One2many('allergy.image', 'product_tmpl_id', string="Allergy Icons")
    conservation_of_pack = fields.Char(string="Conservation of Pack")
    product_use = fields.Char(string="Product Use")
    ingredients = fields.Text(string="ingredients")


class EnergeticValue(models.Model):
    _name = "energetic.value"

    name = fields.Char(string="Name")
    template_id = fields.Many2one('product.template', string="Product")
    enargy_id = fields.Many2one('product.enargy', string="Enargy")


class ProductEnargy(models.Model):
    _name = "product.enargy"

    name = fields.Char(string="Name", required=True)


class AllergyImage(models.Model):
    _name = 'allergy.image'

    name = fields.Char('Name')
    image = fields.Binary('Image', attachment=True)
    product_tmpl_id = fields.Many2one('product.template', 'Related Product', copy=True)