# -*- coding: utf-8 -*-
# from odoo import http


# class RequestMaterial(http.Controller):
#     @http.route('/request_material/request_material/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/request_material/request_material/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('request_material.listing', {
#             'root': '/request_material/request_material',
#             'objects': http.request.env['request_material.request_material'].search([]),
#         })

#     @http.route('/request_material/request_material/objects/<model("request_material.request_material"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('request_material.object', {
#             'object': obj
#         })
