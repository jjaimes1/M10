# -*- coding: utf-8 -*-
from odoo import http

# class Tasquesjjh(http.Controller):
#     @http.route('/tasquesjjh/tasquesjjh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tasquesjjh/tasquesjjh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tasquesjjh.listing', {
#             'root': '/tasquesjjh/tasquesjjh',
#             'objects': http.request.env['tasquesjjh.tasquesjjh'].search([]),
#         })

#     @http.route('/tasquesjjh/tasquesjjh/objects/<model("tasquesjjh.tasquesjjh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tasquesjjh.object', {
#             'object': obj
#         })