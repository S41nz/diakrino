# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a la prensa que tiene un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class PerfilPrensa:
    '''
    Atributos
    '''
    #Referencia a las noticias acumuladas para un analisis determinado
    noticias = []

    def __init__(self, perfil_id):
        '''
        Constructor
        '''
        self.perfil_id = perfil_id

    def get_noticias(self):
        return self.noticias


    def get_perfil_id(self):
        return self.perfil_id


    def get_word_cloud(self):
        return self.word_cloud


    def get_analisis_sentimiento(self):
        return self.analisis_sentimiento


    def set_noticias(self, value):
        self.noticias = value


    def set_word_cloud(self, value):
        self.word_cloud = value


    def set_analisis_sentimiento(self, value):
        self.analisis_sentimiento = value

        