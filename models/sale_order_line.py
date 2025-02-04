# -*- coding: utf-8 -*-
from odoo import models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # No necesitamos un @api.onchange para el dominio, pues se definirá vía XML.
    # Aquí podrías añadir lógica adicional si la requieres más adelante.
    pass
