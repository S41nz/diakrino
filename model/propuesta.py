# -*- coding: latin-1 -*-
'''
Clase modelo que representa una propuesta correspondiente a la plataforma de un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class Propuesta:
    '''
    Atributos
    '''


    def __init__(self, propuesta_id):
        '''
        Constructor
        '''
        self.propuesta_id = propuesta_id

    def get_propuesta_id(self):
        return self.propuesta_id


    def get_tipo_propuesta(self):
        return self.tipo_propuesta


    def get_titulo(self):
        return self.titulo


    def get_descripcion(self):
        return self.descripcion


    def set_tipo_propuesta(self, value):
        self.tipo_propuesta = value


    def set_titulo(self, value):
        self.titulo = value


    def set_descripcion(self, value):
        self.descripcion = value

        