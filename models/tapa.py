from odoo import models, fields, api

class Tapa(models.Model):
    _name = 'bar.tapa'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Float('Cantidad', required=True)
    llevar = fields.Boolean('Para Llevar', required=True)
    comida = fields.Many2one('bar.comida', 'Comida')
    bebida = fields.Many2one('bar.bebida', 'Bebida')

    @api.one
    def aniadir(self):
        self.cantidad = self.cantidad + 1
