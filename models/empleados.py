from odoo import models, fields

class Empleados(models.Model):
    _name = 'bar.empleados'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    direccion = fields.Char('Direccion', required=False)
    
