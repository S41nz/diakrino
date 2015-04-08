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
    #Lista de perfiles de contacto que puede tener un candidato determinado
    info_contacto = []
    #Lista de perfiles virtuales que puede tener un candidato determinado
    info_virtual = []
    #Lista de afiliaciones de un candidato determinado
    info_afiliaciones = []
    #Lista de gente que forma o formará parte de su gabinete y equipo de trabajo
    equipo_trabajo = []
    #Lista de gente relevante que apoya a un candidat determinado
    equipo_apoyo = []

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

    def get_perfil_profesional(self):
        return self.perfil_profesional

    def set_perfil_profesional(self, value):
        self.perfil_profesional = value

    def get_info_contacto(self):
        return self.info_contacto

    def set_info_contacto(self, value):
        self.info_contacto = value

    def get_info_virtual(self):
        return self.info_virtual

    def set_info_virtual(self, value):
        self.info_virtual = value

    def get_perfil_prensa(self):
        return self.perfil_prensa

    def set_perfil_prensa(self, value):
        self.perfil_prensa = value
   
    def get_perfil_plataforma(self):
        return self.perfil_plataforma

    def set_perfil_plataforma(self, value):
        self.perfil_plataforma = value

    def get_equipo_trabajo(self):
        return self.equipo_trabajo

    def get_equipo_apoyo(self):
        return self.equipo_apoyo

    def set_equipo_trabajo(self, value):
        self.equipo_trabajo = value

    def set_equipo_apoyo(self, value):
        self.equipo_apoyo = value







    


     
