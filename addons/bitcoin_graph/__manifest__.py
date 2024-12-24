{
    'name': 'Bitcoin Price Tracker',
    'version': '18.0.1.0.0',
    'category': 'Website',
    'summary': 'Bitcoin Price Tracker Snippet',
    'description': """
        This module adds a snippet to display Bitcoin price chart on your website.
    """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/snippets/bitcoin_chart_template.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # Chart.js dependency
            ('include', 'https://cdn.jsdelivr.net/npm/chart.js'),
            # Module assets
            '/bitcoin_graph/static/src/js/bitcoin_chart.js',
            '/bitcoin_graph/static/src/css/bitcoin_chart.css',
            '/bitcoin_graph/static/src/xml/bitcoin_chart.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
