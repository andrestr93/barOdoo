from odoo import models, fields

class Comida(models.Model):
    _name = 'bar.comida'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    tipo = fields.Char('Tipo', required=True)
    fechcad = fields.Char('Fecha Caducidad', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
