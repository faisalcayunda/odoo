# -*- coding: utf-8 -*-
{
    'name': 'HR Refresh',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Custom HR extensions',
    'sequence': 1,
    'description': """
        Custom HR extensions including random jobs snippet
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
        'website',
        'website_hr_recruitment',
    ],
    'data': [
        'views/snippets/random_jobs_snippet.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hr_refresh/static/src/js/random_jobs.js',
            'hr_refresh/static/src/css/random_jobs.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'demo': [
        'demo/demo.xml',
    ],
}
