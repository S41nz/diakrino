# -*- coding: latin-1 -*-
'''
Clase modelo que representa el perfil de un partido político determinado que participa en un proceso electoral dado
Created on 07/04/2015

@author: S41inz
'''

class PerfilPartido:
    '''
    Atributos
    '''


    def __init__(self, partido_id):
        
        self.partido_id = partido_id

    def get_partido_id(self):
        return self.partido_id


    def get_nombre(self):
        return self.nombre


    def get_siglas(self):
        return self.siglas


    def get_tipo_ala(self):
        return self.tipo_ala


    def get_ruta_logo(self):
        return self.ruta_logo


    def get_resena(self):
        return self.resena


    def set_nombre(self, value):
        self.nombre = value


    def set_siglas(self, value):
        self.siglas = value


    def set_tipo_ala(self, value):
        self.tipo_ala = value


    def set_ruta_logo(self, value):
        self.ruta_logo = value


    def set_resena(self, value):
        self.resena = value

        
        