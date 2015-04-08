# -*- coding: latin-1 -*-
'''
Clase modelo que representa una noticia determinada que hace referencia a uno o más candidatos
Created on 08/04/2015

@author: S41nz
'''

class Noticia:
    '''
    Atributos
    '''


    def __init__(self, noticia_id):
        '''
        Constructor
        '''
        self.noticia_id = noticia_id

    def get_noticia_id(self):
        return self.noticia_id


    def get_titulo(self):
        return self.titulo


    def get_contenido(self):
        return self.contenido


    def get_fuente(self):
        return self.fuente


    def get_fecha(self):
        return self.fecha


    def set_titulo(self, value):
        self.titulo = value


    def set_contenido(self, value):
        self.contenido = value


    def set_fuente(self, value):
        self.fuente = value


    def set_fecha(self, value):
        self.fecha = value
