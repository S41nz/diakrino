# -*- coding: latin-1 -*-
'''
Definición de un colector de datos abstracto para poder extraer información requerida de una fuente determinada

@author: SA1nz
'''

from abc import  ABCMeta, abstractmethod

class BaseCollector:
    
    __metaclass__ = ABCMeta
    '''
    Atributos
    '''
    #Bandera para determinar el estado actual de la colección de datos
    collectionStatus = ""
    
    #Diccionario para los parámetros de entrada para el colector
    collectorParams = {}
    
    #Diccionario para las opciones que haya para un colector determinado
    collectionOptions = {}
    
    #Diccionario para documentar y poder comunicar las opciones de colección soportadas por un colector determinado
    supportedCollectionOptions = {}

    def __init__(self, params):
        '''
        Constructor
        '''
    @abstractmethod
    def initialize(self):
        '''
        Método para ejecutarse previo a la collección de datos
        '''
    @abstractmethod
    def collect(self):
        '''
        Definición de método para llevar a cabo la colección de datos en base a los parametros previamente mandados
        '''
    
    def setCollectionOptions(self,options):
        '''
        Método para establecer las opciones (si aplican) para considerarse para una colección de datos determinada
        e.g. un filtro sobre los datos
        '''
        self.collectionOptions = options
    
    def getSupportedCollectionOptions(self):
        '''
        Método que comunica cuales son las opciones soportadas por el colector
        '''
        return self.supportedCollectionOptions
    
    @abstractmethod    
    def getData(self):
        '''
        Definición de método para obtener los datos recolectados
        '''
    
    def getStatus(self):
        '''
        Método para obtener el status de la colección de datos
        '''
        return self.collectionStatus
    