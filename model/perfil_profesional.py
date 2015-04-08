# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a la trayectoria profesional de un candidato determinado
Created on 07/04/2015

@author: S41nz
'''

class PerfilProfesional(object):
    '''
    Atributos
    '''
    trayectoria = []

    def __init__(self, perfil_id):
        '''
        Constructor
        '''
        self.perfil_id = perfil_id

    def get_trayectoria(self):
        return self.trayectoria


    def get_perfil_id(self):
        return self.perfil_id


    def get_cargo_actual(self):
        return self.cargo_actual


    def set_trayectoria(self, value):
        self.trayectoria = value


    def set_cargo_actual(self, value):
        self.cargo_actual = value
