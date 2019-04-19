# -*- coding: utf-8 -*-
{
    'name': "SojitzVN Inventory Warnings",

    'summary': """
        Show warning messages on Inventory Dashboard
    """,

    'description': """
        Show warning messages on Inventory Dashboard
    """,

    'author': "Nissho Electronics Vietnam Company Limited",
    'website': "http://www.nissho-vn.com/en/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inventory_overviews.xml',
    ],
}