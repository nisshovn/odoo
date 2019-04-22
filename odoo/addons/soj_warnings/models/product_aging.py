# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.fields import Date as fDate
from dateutil import relativedelta


class ProductAging(models.Model):
    _inherit = 'stock.quant'

    # Product Age Category
    product_age_cat = fields.Char(string='Age Category', default=_('0 - 3 months'))

    # TODO: Create overdue date to store the date of expired => for product age warning popup
    # overdue_date = fields.Date(string='Overdue date', compute='_compute_overdue', store=True)

    # Cron job run everyday to calculate product age
    @api.model
    def compute_age_cat(self):
        self.search([
            ('in_date', '>', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=3))),
        ]).write({
            'product_age_cat': _('0 - 3 months')
        })

        self.search([
            ('in_date', '<=', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=3))),
            ('in_date', '>', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=6))),
        ]).write({
            'product_age_cat': _('3 - 6 months')
        })

        self.search([
            ('in_date', '<=', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=6))),
            ('in_date', '>', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=12))),
        ]).write({
            'product_age_cat': _('6 - 12 months')
        })

        self.search([
            ('in_date', '<=', fields.Date.to_string(fDate.today() - relativedelta.relativedelta(months=12))),
        ]).write({
            'product_age_cat': _('Over 12 months')
        })
        return True
