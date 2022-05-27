# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Send Mail Custommer',
    'category': '',
    'author': 'rivo2302',
    'summary': 'Send mail toa customer',
    'version': '1.0.0',
    'description': """
This module is for sending mail to a customer.
    """,
    'depends': ['mrp','mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production_form.xml',
        'data/template.xml',
        
    ],
    'installable': True,
    'assets': {
    },
    'license': 'LGPL-3',
}
