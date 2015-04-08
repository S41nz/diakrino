# -*- coding: latin-1 -*-
'''
Clase modelo que representa información respecto a diferentes maneras en las que un candidato determinado esta dado de alta en Internet
Created on 08/04/2015

@author: S41nz
'''

class PerfilVirtual:
    '''
    Atributos
    '''


    def __init__(self, perfil_id):
        '''
        Constructor
        '''
        self.perfil_id = perfil_id

    def get_perfil_id(self):
        return self.perfil_id


    def get_tipo_cuenta(self):
        return self.tipo_cuenta


    def get_nombre_usuario(self):
        return self.nombre_usuario


    def get_url(self):
        return self.url


    def get_app_id(self):
        return self.app_id


    def get_info_adicional(self):
        return self.info_adicional


    def set_tipo_cuenta(self, value):
        self.tipo_cuenta = value


    def set_nombre_usuario(self, value):
        self.nombre_usuario = value


    def set_url(self, value):
        self.url = value


    def set_app_id(self, value):
        self.app_id = value


    def set_info_adicional(self, value):
        self.info_adicional = value

        
        