# -*- coding: latin-1 -*-
'''
Clase modelo que representa el perfil académico de una persona (candidato) determinado
Created on 07/04/2015

@author: S41nz
'''

class PerfilAcademico:
    '''
    Atributos
    '''
    trayectoria = []

    def __init__(self, perfil_id):
        
        self.perfil_id = perfil_id
        
    def get_trayectoria(self):
        return self.trayectoria


    def get_perfil_id(self):
        return self.perfil_id


    def get_grado_actual(self):
        return self.grado_actual


    def set_trayectoria(self, value):
        self.trayectoria = value


    def set_grado_actual(self, value):
        self.grado_actual = value

