# -*- coding: latin-1 -*-
from engine.enums.engine_status import EngineStatus
from model.proceso_electoral import ProcesoElectoral
from model.entidad import Entidad
from model.enums.categoria_entidad import CategoriaEntidad
from collection.googlesheets.googlesheet_collector import GoogleSheetsCollector
from collection.enums.coleccion_status import ColeccionStatus

import logging
import datetime
import os

'''
Clase que se encarga de cargar, mantener y actualizar los modelos de metadata que estén disponibles para análisis y consulta
Created on 08/04/2015

@author: S41nz
'''

class ModelManager:
    '''
    Atributos
    '''
    modelos = {}
    cache_candidatos = {}
    cache_entidades = {}

    def __init__(self):
        '''
        Constructor
        '''
        #Creamos el logger correspondiente del manager del modelo
        self.logger = logging.getLogger("ModelManager") 
        self.status = EngineStatus.CREADO
        
    def initialize(self):
        '''
        Método para inicializar la instancia del Model Manager
        '''
        #Cargamos el modélo
        self.loadModel(False)
        
        #Notificamos que terminamos de cargar el modelo y estamos listos
        self.status = EngineStatus.LISTO
    
    def loadModel(self,refresh=False):
        '''
        Método para cargar el modelo y/o refrescarlo bajo demanda
        '''
        #Notificamos que estamos cargando la información
        self.status = EngineStatus.PROCESANDO
        
        #Cargamos el modelo
        nuevoPeriodo = datetime.date(2015,06,01)
        self.loadProcesoElectoral('PE_ZMG_2015', "Elecciones Intermedias ZMG 2015", nuevoPeriodo)
        
        #Load the entity instances
        #Guadalajara
        self.loadEntidades('PE_ZMG_2015', 'GDL', 'Guadalajara', CategoriaEntidad.MUNICIPIO)
        #Zapopan
        self.loadEntidades('PE_ZMG_2015', 'ZPN', 'Zapopan', CategoriaEntidad.MUNICIPIO)
        
        self.status = EngineStatus.EXITO
        
    def getStatus(self):
        '''
        Método para comunicar el estado actual de la instancia del ModelManager
        '''
        return self.status
    
    def loadProcesoElectoral(self,proceso_id,nombre_proceso,periodo):
        '''
        Method to create a given Electoral Process model
        '''
        procesoElectoral = ProcesoElectoral(proceso_id,nombre_proceso,periodo)
        #Añadimos la instancia del modelo
        self.modelos[proceso_id] = procesoElectoral
        
    
    def loadEntidades(self,proceso_id,entidad_id,name,entidad_type):
        '''
        Method to load the corresponding entities for a given elections process
        '''
        #Create the entity instance
        entity = Entidad(entidad_id)
        #Set the name
        entity.set_nombre(name)
        #Set the entity Type
        entity.set_tipo_entidad(entidad_type)
        
        #Check if the entity list has been initialized yet
        if self.modelos[proceso_id].get_entidades() == None:
            self.modelos[proceso_id].set_entidades([])
        
        #Now add the entity
        self.modelos[proceso_id].get_entidades().append(entity)
        
        self.logger.info("Creada la metadata de la entidad: "+str(entidad_id) + " para el proceso electoral: "+str(proceso_id))
    
    def loadCandidates(self,targetEntity):
        '''
        Method to load all the metadata from the candidates
        '''
        
        #Load all the parameters for the corresponding spreadsheet collector
        collectorParams = {}
        collectorParams['username'] = os.environ['DIAKRINO_GOOGLE_DRIVE_USERNAME']
        collectorParams['password'] = os.environ['DIAKRINO_GOOGLE_DRIVE_PASSWORD']
        collectorParams['source_id'] = os.environ['DIAKRINO_GOOGLE_DRIVE_CANDIDATES_SPREADSHEET_NAME']
        collectorParams['spreadsheet_key'] = os.environ['DIAKRINO_GOOGLE_DRIVE_CANDIDATES_SPREADSHEET_KEY']
        collectorParams['worksheet_id'] = os.environ['DIAKRINO_GOOGLE_DRIVE_CANDIDATES_WORKSHEET_ID']
        
        #Initialize the collector
        spreadsheetCollector = GoogleSheetsCollector(collectorParams)
        
        spreadsheetCollector.initialize()
        
        #Collect the data
        spreadsheetCollector.collect()
        
        if spreadsheetCollector.getStatus() == ColeccionStatus.EXITO:
            #For the moment print the collected data on the console
            spreadsheetCollector.printResult(spreadsheetCollector.getData())
        
    def getModels(self):
        '''
        Método para obtener los modelos disponibles en la cache
        '''
        
        #Consideremos los casos cuando no fue posible
        if self.status != EngineStatus.LISTO:
            return {}
        
        #Considerando que si se pudo cargar el modelo, procesamos la solicitud
        return self.modelos
        
        
            
    def getModel(self,model_id):
        '''
        Método para obtener la referencia de un modelo determinado
        '''
        
        #Validamos la entrada
        if model_id is None:
            return None
        
        #Checamos primero el estado interno de la instancia para verificar
        if self.status != EngineStatus.LISTO:
            self.logger.warn('Intento fallido de obtener el modelo con el id '+str(model_id)+' el ModelManager no estaba listo')
            return None
        
        #Check for key existence
        if model_id not in self.modelos.keys():
            return None
        #Procesamos la solicitud
        return self.modelos[model_id]
        
    def loadCacheWithModel(self,model_id):
        '''
        Método para cargar la cache de candidatos y entidades basada en un modelo de proceso de elecciones determinado
        '''
        
        #Validamos la entrada
        if model_id is None:
            return None
        
        #Checamos primero el estado interno de la instancia para verificar
        if self.status != EngineStatus.LISTO:
            self.logger.warn('Intento fallido de cargar la cache con el modelo con el id '+str(model_id)+' el ModelManager no estaba listo')
            return None
        
        #TODO: Cargar todas las entidades y candidatos aquí
        
        
        