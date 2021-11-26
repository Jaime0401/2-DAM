# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Jugadores(models.Model):
    _name = "jugadores"

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    altura = fields.Char(string="Altura del jugador")
    equipo = fields.Many2one("equipos", string="Equipo")

class Equipos(models.Model):
    _name = "equipos"

    name = fields.Char(string="Nombre")
    ciudad = fields.Char(string="Ciudad")
    conferencia = fields.Selection([('0', 'Este'),('1', 'Oeste')])
    jugadores = fields.One2many("jugadores", "equipo", string="Jugadores")

