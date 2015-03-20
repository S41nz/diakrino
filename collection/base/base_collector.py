# -*- coding: latin-1 -*-
'''
Definici�n de un colector de datos abstracto para poder extraer informaci�n requerida de una fuente determinada

@author: SA1nz
'''

class BaseCollector:
    
    '''
    Atributos
    '''
    #Bandera para determinar el estado actual de la colecci�n de datos
    collectionStatus = ""
    
    #Diccionario para los par�metros de entrada para el colector
    collectorParams = {}
    
    #Diccionario para las opciones que haya para un colector determinado
    collectionOptions = {}

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def initialize(self):
        '''
        M�todo para ejecutarse previo a la collecci�n de datos
        '''
    
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
        
        
    def getData(self):
        '''
        Definici�n de m�todo para obtener los datos recolectados
        '''
    
    def getStatus(self):
        '''
        M�todo para obtener el status de la colecci�n de datos
        '''
        return self.collectionStatus
    