# -*- coding: latin-1 -*-
'''
Definici�n de un colector de datos abstracto para poder extraer informaci�n requerida de una fuente determinada

@author: SA1nz
'''

from abc import  ABCMeta, abstractmethod

class BaseCollector:
    
    __metaclass__ = ABCMeta
    '''
    Atributos
    '''
    #Bandera para determinar el estado actual de la colecci�n de datos
    collectionStatus = ""
    
    #Diccionario para los par�metros de entrada para el colector
    collectorParams = {}
    
    #Diccionario para las opciones que haya para un colector determinado
    collectionOptions = {}
    
    #Diccionario para documentar y poder comunicar las opciones de colecci�n soportadas por un colector determinado
    supportedCollectionOptions = {}

    def __init__(self, params):
        '''
        Constructor
        '''
    @abstractmethod
    def initialize(self):
        '''
        M�todo para ejecutarse previo a la collecci�n de datos
        '''
    @abstractmethod
    def collect(self):
        '''
        Definici�n de m�todo para llevar a cabo la colecci�n de datos en base a los parametros previamente mandados
        '''
    
    def setCollectionOptions(self,options):
        '''
        M�todo para establecer las opciones (si aplican) para considerarse para una colecci�n de datos determinada
        e.g. un filtro sobre los datos
        '''
        self.collectionOptions = options
    
    def getSupportedCollectionOptions(self):
        '''
        M�todo que comunica cuales son las opciones soportadas por el colector
        '''
        return self.supportedCollectionOptions
    
    @abstractmethod    
    def getData(self):
        '''
        Definici�n de m�todo para obtener los datos recolectados
        '''
    
    def getStatus(self):
        '''
        M�todo para obtener el status de la colecci�n de datos
        '''
        return self.collectionStatus
    