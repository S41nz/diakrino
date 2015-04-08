# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a un evento determinado que comprende la trayectoria profesional de un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class Cargo:
    '''
    Atributos
    '''


    def __init__(self, evento_id):
        '''
        Constructor
        '''
        self.evento_id = evento_id

    def get_evento_id(self):
        return self.evento_id


    def get_tipo_sector(self):
        return self.tipo_sector


    def get_organizacion(self):
        return self.organizacion


    def get_nombre_cargo(self):
        return self.nombre_cargo


    def get_fecha_inicio(self):
        return self.fecha_inicio


    def get_fecha_terminacion(self):
        return self.fecha_terminacion


    def get_descripcion(self):
        return self.descripcion


    def get_ruta_logo(self):
        return self.ruta_logo


    def set_tipo_sector(self, value):
        self.tipo_sector = value


    def set_organizacion(self, value):
        self.organizacion = value


    def set_nombre_cargo(self, value):
        self.nombre_cargo = value


    def set_fecha_inicio(self, value):
        self.fecha_inicio = value


    def set_fecha_terminacion(self, value):
        self.fecha_terminacion = value


    def set_descripcion(self, value):
        self.descripcion = value


    def set_ruta_logo(self, value):
        self.ruta_logo = value

