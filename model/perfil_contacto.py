# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a diferentes maneras de contactar que tiene un candidato determinado
Created on 08/04/2015

@author: S41nz
'''

class PerfilContacto:
    '''
    Atributos
    '''


    def __init__(self, contacto_id):
        '''
        Constructor
        '''
        self.contacto_id = contacto_id

    def get_contacto_id(self):
        return self.contacto_id


    def get_tipo_contacto(self):
        return self.tipo_contacto


    def get_info_contacto(self):
        return self.info_contacto


    def get_descripcion_contacto(self):
        return self.descripcion_contacto


    def set_tipo_contacto(self, value):
        self.tipo_contacto = value


    def set_info_contacto(self, value):
        self.info_contacto = value


    def set_descripcion_contacto(self, value):
        self.descripcion_contacto = value

        