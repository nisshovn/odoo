# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cmdtycd = fields.Char('Commodity Code', store=True)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_cmdtycd = fields.Char('Commodity Code', related='product_id.cmdtycd', store=True)
