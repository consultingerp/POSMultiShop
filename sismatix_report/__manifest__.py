# -*- coding: utf-8 -*-
{
    'name': 'Dynamic Tree View',
    'version': '1.0.1',
    'author': "Eman Taha",
    'website': 'emeytahaz@gmail.com',
    'category': 'Other',
    'sequence': 20,
    'summary': 'Dynamic Tree View',
    'depends': ['web'],
    'data': [
        'security/sismatix_security.xml',
        'views/ir_model_fields_view.xml',
        'views/sismatix_report.xml',
        'report/report_sismatix.xml',
        'wizard/change_tree_fields_view.xml',
        'views/sismatix_report_assets.xml',
    ],
    'demo': [
    ],
    'qweb': [
        "static/src/xml/*.xml",
        # "static/src/xml/web_print_view_template.xml",
        # "static/src/xml/web_export_view_template.xml",
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
    'price': 200,
    'currency': 'EUR',
}
