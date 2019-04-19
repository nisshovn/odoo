# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date as fDate
from dateutil import relativedelta


class ProductAging(models.Model):
    _inherit = 'stock.quant'

    # Product Age Category
    product_age_cat = fields.Char(string='Age Category', compute='_compute_age_cat', store=True, default='0 - 3 months')

    # TODO: Create overdue date to store the date of expired => for product age warning popup
    # overdue_date = fields.Date(string='Overdue date', compute='_compute_overdue', store=True)

    @api.depends('in_date')
    def _compute_age_cat(self):
        today = fDate.from_string(fDate.today())
        for product in self.filtered('in_date'):
            no_of_months = relativedelta.relativedelta(today, product.in_date).months
            if no_of_months <= 3:
                product.product_age_cat = '0 - 3 months'
            elif 3 < no_of_months <= 6:
                product.product_age_cat = '3 - 6 months'
            elif 6 < no_of_months <= 12:
                product.product_age_cat = '6 - 12 months'
            else:
                product.product_age_cat = 'Over 12 months'
