# -*- coding: utf-8 -*-
{
    "name": "Sale Partner Filter",
    "version": "15.0.1.0.0",  # Ajusta a la convención de Odoo 17 si deseas
    "summary": "Filtra productos en líneas de venta según company_registry del cliente.",
    "author": "Alphaqueb Consulting SAS",
    "website": "https://alphaqueb.com",
    "category": "Sales",
    "license": "AGPL-3",
    "depends": [
        "sale",
    ],
    "data": [
        "views/sale_order_line_view.xml",
    ],
    "installable": True,
    "application": False,
}
