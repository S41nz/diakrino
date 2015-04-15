# -*- coding: latin-1 -*-
'''
Clase padre dentro del modelo. Representa el proceso de unas elecciones determinadas
Created on 25/03/2015

@author: S41inz
'''

class ProcesoElectoral:
    
    '''
    Atributos
    '''
    #Lista de las entidades involucradas en el proceso electoral
    entidades = []
    
    def __init__(self, id_proceso,nombre_proceso,periodo_proceso):
        #Asignamos el ID del proceso electoral
        self.id = id_proceso
        #Asignamos el nombre del proceso electoral
        self.nombre = nombre_proceso
        #Asignamos el periodo del proceso electoral
        self.periodo = periodo_proceso

    def get_entidades(self):
        return self.entidades


    def set_entidades(self, value):
        self.entidades = value


    def get_id(self):
        return self.id


    def get_nombre(self):
        return self.nombre


    def get_periodo(self):
        return self.periodo


    def set_nombre(self, value):
        self.nombre = value


    def set_periodo(self, value):
        self.periodo = value
    

