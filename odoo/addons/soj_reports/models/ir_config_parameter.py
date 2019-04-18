# -*- coding: utf-8 -*-
import odoo
from odoo import models


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self, force=False):
        super(IrConfigParameter, self).init(force=force)
        self.set_param('http.report', odoo.tools.config['http_report'])
