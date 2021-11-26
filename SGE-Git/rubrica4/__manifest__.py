# -*- coding: utf-8 -*-
{
    'name': "rubrica4",
    'summary': """Rubrica4""",
    'description': """
        Rubrica 4:
    """,
    'author': "Jaime Andreu",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rubrica',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}