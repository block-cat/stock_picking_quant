# -*- coding: utf-8 -*-
from odoo import http

# class StockPickingQuant(http.Controller):
#     @http.route('/stock_picking_quant/stock_picking_quant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_picking_quant/stock_picking_quant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_picking_quant.listing', {
#             'root': '/stock_picking_quant/stock_picking_quant',
#             'objects': http.request.env['stock_picking_quant.stock_picking_quant'].search([]),
#         })

#     @http.route('/stock_picking_quant/stock_picking_quant/objects/<model("stock_picking_quant.stock_picking_quant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_picking_quant.object', {
#             'object': obj
#         })