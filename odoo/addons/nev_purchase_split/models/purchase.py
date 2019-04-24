# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class NEVPurchaseSplit(models.Model):
    _inherit = 'purchase.order'
    _parent_name = 'parent_id'
    _parent_store = True

    parent_id = fields.Many2one(comodel_name='purchase.order', index=True, string='Splitted From PO',
                                help='PO Splited From Ref:', ondelete='restrict')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('purchase.order', 'parent_id', 'Child PO')

    parent_amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True,
                                            compute='_parent_amount_all')
    parent_amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_parent_amount_all')
    parent_amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_parent_amount_all')
    child_count = fields.Integer(string='Number of child PO', default=0)

    @api.one
    @api.depends('child_ids')
    def _parent_amount_all(self):
        parent_amount_untaxed = parent_amount_tax = 0.0
        for order in self.child_ids:
            parent_amount_untaxed += order.amount_untaxed
            parent_amount_tax += order.amount_tax
            self.update({
                # TODO: consider to uncomment for displaying Total amount in PO tree view (and hide all child PO)
                # 'amount_untaxed': parent_amount_untaxed,
                # 'amount_tax': parent_amount_tax,
                # 'amount_total': parent_amount_untaxed + parent_amount_tax,

                'parent_amount_untaxed': parent_amount_untaxed,
                'parent_amount_tax': parent_amount_tax,
                'parent_amount_total': parent_amount_untaxed + parent_amount_tax,
            })

    @api.multi
    def button_split(self):
        """
        This function splits a PO to multiple child PO base on Scheduled Date (date_planned)
        """
        for order in self:
            if order.order_line:
                # Select distinct scheduled dates
                dates = {line.date_planned.date() for line in order.order_line}

                # If it has only 1 scheduled date, do nothing
                if dates and len(dates) == 1:
                    continue

                # Create new child PO for each Scheduled date
                for d_date in dates:
                    new_po = super(NEVPurchaseSplit, self).copy()
                    new_po.write({
                        'parent_id': order.id,
                        'date_planned': d_date
                    })

                    if new_po:
                        for i, li in enumerate(new_po.order_line):
                            # Correct date_planned for child PO
                            li.write({
                                'date_planned': order.order_line[i].date_planned
                            })
                            if relativedelta(li.date_planned, d_date).days != 0:
                                li.unlink()

                # Set number of child for parent PO
                self.update({
                    'child_count': len(dates)
                })

                # Unlink order_line in the parent PO
                for line in order.order_line:
                    self.env['purchase.order.line'].browse(line.id).unlink()
        return {}
