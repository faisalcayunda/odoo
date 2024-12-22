# -*- coding: utf-8 -*-
# from odoo import http


# class HrRefresh(http.Controller):
#     @http.route('/hr_refresh/hr_refresh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_refresh/hr_refresh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_refresh.listing', {
#             'root': '/hr_refresh/hr_refresh',
#             'objects': http.request.env['hr_refresh.hr_refresh'].search([]),
#         })

#     @http.route('/hr_refresh/hr_refresh/objects/<model("hr_refresh.hr_refresh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_refresh.object', {
#             'object': obj
#         })

