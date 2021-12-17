# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Personas(models.Model):
    _name = "personas"

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")

class Jugadores(models.Model):
    _inherit = 'personas'
    _name = "jugadores"

    altura = fields.Char(string="Altura del jugador")
    equipo = fields.Many2one("equipos", string="Equipo")
    puntosp1 = fields.Float(String="Puntos Partido 1", digits=(12, 2))
    puntosp2 = fields.Float(String="Puntos Partido 2", digits=(12, 2))
    puntosp3 = fields.Float(String="Puntos Partido 3", digits=(12, 2))
    puntosp4 = fields.Float(String="Puntos Partido 4", digits=(12, 2))
    puntosp5 = fields.Float(String="Puntos Partido 5", digits=(12, 2))
    media_puntos = fields.Float(String="Media Puntos", compute='mediapuntos')

    @api.depends('puntosp1', 'puntosp2', 'puntosp3', 'puntosp4', 'puntosp5')              
    def mediapuntos(self):
        for record in self:
            record.media_puntos = (record.puntosp1 + record.puntosp2 + record.puntosp3 + record.puntosp4 + record.puntosp5) / 5

class Equipos(models.Model):
    _name = "equipos"

    name = fields.Char(string="Nombre")
    ciudad = fields.Char(string="Ciudad")
    conferencia = fields.Selection([('0', 'Este'),('1', 'Oeste')])
    jugadores = fields.One2many("jugadores", "equipo", string="Jugadores")


