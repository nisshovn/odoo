# -*- coding: utf-8 -*-
{
    'name': "Reports for Sojitz Vietnam",

    'summary': """
        Reports for Sales department in Sojitz Vietnam""",

    'description': """
        The list of reports are mentioned below:
        - TS_Upload Purchases 
        - TS_Upload Sales 
        - TS_Upload Stock Exchanges
        - Gross Profit
        - Stock report
        - Monthly
        - OA&HA
    """,

    'author': "Nissho Electronics Vietnam Company Limited",
    'website': "http://www.nissho-vn.com/en/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}