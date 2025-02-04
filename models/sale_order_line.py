# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('order_id.partner_id')
    def _onchange_partner_id(self):
        """
        Cuando se cambia el cliente (partner_id) en la orden,
        filtramos los productos cuyo default_code contenga el
        company_registry del partner.
        """
        if self.order_id.partner_id.company_registry:
            company_registry = self.order_id.partner_id.company_registry
            return {
                'domain': {
                    'product_id': [
                        ('default_code', 'ilike', company_registry)
                    ]
                }
            }
        else:
            # Si el partner no tiene company_registry o está vacío,
            # decides si mostrar todos los productos o ninguno.
            return {
                'domain': {
                    'product_id': []
                }
            }
