# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a un evento determinado que comprende la trayectoria académica de un candidato determinado
Created on 07/04/2015

@author: S41nz
'''

class Educacion:
    '''
    Atributos
    '''


    def __init__(self, evento_id):

        self.evento_id = evento_id

    def get_evento_id(self):
        return self.evento_id


    def get_tipo_grado(self):
        return self.tipo_grado


    def get_institucion(self):
        return self.institucion


    def get_fecha_inicio(self):
        return self.fecha_inicio


    def get_fecha_terminacion(self):
        return self.fecha_terminacion


    def get_descripcion(self):
        return self.descripcion


    def get_ruta_logo(self):
        return self.ruta_logo


    def set_tipo_grado(self, value):
        self.tipo_grado = value


    def set_institucion(self, value):
        self.institucion = value


    def set_fecha_inicio(self, value):
        self.fecha_inicio = value


    def set_fecha_terminacion(self, value):
        self.fecha_terminacion = value


    def set_descripcion(self, value):
        self.descripcion = value


    def set_ruta_logo(self, value):
        self.ruta_logo = value

