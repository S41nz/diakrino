# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a una afiliación que tiene actualmente un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class Afiliacion:
    '''
    Atributos
    '''


    def __init__(self, afiliacion_id):
        '''
        Constructor
        '''
        self.afiliacion_id = afiliacion_id

    def get_afiliacion_id(self):
        return self.afiliacion_id


    def get_nombre_institucion(self):
        return self.nombre_institucion


    def get_descripcion(self):
        return self.descripcion


    def get_url(self):
        return self.url


    def set_nombre_institucion(self, value):
        self.nombre_institucion = value


    def set_descripcion(self, value):
        self.descripcion = value


    def set_url(self, value):
        self.url = value

        
        