# -*- coding: latin-1 -*-
'''
Clase que representa toda la metadata relevante de un candidato en específico
Created on 25/03/2015

@author: S41inz
'''

class Candidato:
    '''
    Atributos
    '''


    def __init__(self, candidato_id):
        '''
        Constructor
        '''
        self.id = candidato_id  
        
    def get_id(self):
        return self.id


    def get_perfil_basico(self):
        return self.perfil_basico


    def set_perfil_basico(self, value):
        self.perfil_basico = value

    def get_perfil_partido(self):
        return self.perfil_partido


    def set_perfil_partido(self, value):
        self.perfil_partido = value

    def get_perfil_academico(self):
        return self.perfil_academico


    def set_perfil_academico(self, value):
        self.perfil_academico = value


     
