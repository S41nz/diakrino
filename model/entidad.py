# -*- coding: latin-1 -*-
'''
Clase modelo que representa una entidad en la cual se lleva a cabo un proceso electoral
Created on 07/04/2015

@author: S41inz
'''

class Entidad:
    '''
    Atributos
    '''
    #Lista de candidatos que compiten por la entidad en cuestion
    candidatos = []
    #Lista de subentidades con su respectivo proceso electoral
    subentidades = []

    def __init__(self, entidad_id):

        self.entidad_id = entidad_id

    def get_candidatos(self):
        return self.candidatos


    def get_subentidades(self):
        return self.subentidades


    def get_entidad_id(self):
        return self.entidad_id


    def get_tipo_entidad(self):
        return self.tipo_entidad


    def get_nombre(self):
        return self.nombre


    def set_candidatos(self, value):
        self.candidatos = value


    def set_subentidades(self, value):
        self.subentidades = value


    def set_tipo_entidad(self, value):
        self.tipo_entidad = value


    def set_nombre(self, value):
        self.nombre = value



        
        