from odoo import models, fields

class Bebida(models.Model):
    _name = 'bar.bebida'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca', required=True)
    precio = fields.Float('Precio', required=True)

##
    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res##