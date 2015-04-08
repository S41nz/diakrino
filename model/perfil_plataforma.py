# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a la plataforma de propuestas que plantea un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class PerfilPlataforma:
    '''
    Atributos
    '''
    propuestas = []

    def __init__(self, plataforma_id):
        '''
        Constructor
        '''
        self.plataforma_id = plataforma_id

    def get_propuestas(self):
        return self.propuestas


    def get_plataforma_id(self):
        return self.plataforma_id


    def get_word_cloud(self):
        return self.word_cloud


    def get_analisis_sentimiento(self):
        return self.analisis_sentimiento


    def set_propuestas(self, value):
        self.propuestas = value


    def set_word_cloud(self, value):
        self.word_cloud = value


    def set_analisis_sentimiento(self, value):
        self.analisis_sentimiento = value

        