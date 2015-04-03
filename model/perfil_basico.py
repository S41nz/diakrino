# -*- coding: latin-1 -*-
'''
Clase que representa la información básica de una persona involucrada en el proceso electoral
Created on 25/03/2015

@author: S41inz
'''

class PerfilBasico:
    '''
    Attributos
    '''


    def __init__(self, perfil_id):
        '''
        Constructor
        '''
        #Asignamos el id de la instancia del perfil
        self.id = perfil_id


    def get_id(self):
        return self.id


    def get_nombre(self):
        return self.nombre


    def get_fecha_de_nacimiento(self):
        return self.fecha_nacimiento


    def get_ala(self):
        return self.ala


    def get_estado_civil(self):
        return self.estado_civil


    def get_ruta_imagen(self):
        return self.ruta_imagen


    def get_tipo_candidatura(self):
        return self.tipo_candidatura


    def get_resena(self):
        return self.resena


    def set_nombre(self, value):
        self.nombre = value


    def set_fecha_de_nacimiento(self, value):
        self.fecha_nacimiento = value


    def set_ala(self, value):
        self.ala = value


    def set_estado_civil(self, value):
        self.estado_civil = value


    def set_ruta_imagen(self, value):
        self.ruta_imagen = value


    def set_tipo_candidatura(self, value):
        self.tipo_candidatura = value


    def set_resena(self, value):
        self.resena = value

        