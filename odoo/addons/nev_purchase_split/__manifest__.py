# -*- coding: utf-8 -*-
{
    'name': "NEV Purchase Order Splitting",

    'summary': """
        Add functionality of Purchase Order splitting""",

    'description': """
        This module will add functionality of Purchase Order Splitting.
    """,

    'author': "Nissho Electronics Vietnam Company Limited",
    'website': "http://www.nissho-vn.com/en/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order.xml',
    ],
}