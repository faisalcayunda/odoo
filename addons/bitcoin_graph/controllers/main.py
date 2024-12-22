from odoo import http
from odoo.http import request


class BitcoinTrackerController(http.Controller):
    @http.route(['/bitcoin_tracker/get_price'], type='json', auth="public", website=True)
    def get_bitcoin_price(self):
        """
        This endpoint can be used for future real-time price updates if needed
        """
        return {
            'success': True
        }
