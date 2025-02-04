# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_registry = fields.Char(
        related="partner_id.company_registry",
        string="Company Registry",
        store=False
    )
