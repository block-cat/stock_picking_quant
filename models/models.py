#!/usr/bin/python3
# @Time    : 2019-07-12
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class stock_move(models.Model):

    _inherit = "stock.move"

    location_qty = fields.Float(
        "当前库存", compute="_get_current_location_qty")

    @api.one
    @api.depends("product_id", "location_id", "location_dest_id")
    def _get_current_location_qty(self):
        # 收货取目的库位
        if self.picking_id.picking_type_id.code not in ("incoming","outgoing"):
            return            
        if self.picking_id.picking_type_id.code == "incoming":
            location_id = self.location_dest_id.id
        # 出库单取源库位
        if self.picking_id.picking_type_id.code == "outgoing":
            location_id = self.location_id.id
        if location_id:
            domain = [("product_id",'=',self.product_id.id),('location_id', '=', location_id)]
            # 批次
            if self.picking_id.picking_type_id.code == "outgoing" and self.lot_id:
                domain.append(('lot_id', '=', self.lot_id.id))

            quants = self.env["stock.quant"].search(domain)
            self.location_qty = sum(quant.quantity for quant in quants)


class stock_move_line(models.Model):

    _inherit = "stock.move.line"

    location_qty = fields.Float(
        "当前库存", compute="_get_current_location_qty")

    @api.one
    @api.depends("product_id", "location_id", "location_dest_id")
    def _get_current_location_qty(self):
        # 收货取目的库位
        if self.picking_id.picking_type_id.code not in ("incoming","outgoing"):
            return            
        if self.picking_id.picking_type_id.code == "incoming":
            location_id = self.location_dest_id.id
        # 出库单取源库位
        if self.picking_id.picking_type_id.code == "outgoing":
            location_id = self.location_id.id
        if location_id:
            domain = [("product_id",'=',self.product_id.id),('location_id', '=', location_id)]
            # 批次
            if self.picking_id.picking_type_id.code == "outgoing" and self.lot_id:
                domain.append(('lot_id', '=', self.lot_id.id))

            quants = self.env["stock.quant"].search(domain)
            self.location_qty = sum(quant.quantity for quant in quants)
