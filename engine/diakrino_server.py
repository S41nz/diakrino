# -*- coding: latin-1 -*-
import logging
import datetime
from engine.model_manager import ModelManager
from engine.enums.engine_status import EngineStatus
from engine.analysis_manager import AnalysisManager


'''
Main class that launches the server which will attend a given request for information.

@author: S41nz
'''

class DiakrinoServer:
    '''
    Atributos
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        #Obtenemos el momento actual cuando se crea la instancia
        now = datetime.datetime.now()
        
        #Construimos el nombre del archivo de logging
        logFileName = "DiakinoServer_"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+".log"
        #Inicializamos el servicio de logging
        logging.basicConfig(filename = logFileName,filemode='w',level = logging.DEBUG,format='[%(levelname)s][%(asctime)s][%(name)s] : %(message)s')
        #Obtenemos la referencia del logger
        self.logger = logging.getLogger('DiakrinoServer')
        
        #Actualmente por default instanciamos el model managers
        self.model_manager = ModelManager()
        
        #Instanciamos el analysis manager
        self.analysis_manager = AnalysisManager()
        
        #Notificamos el status como inicializado
        self.status = EngineStatus.CREADO
        
        self.logger.info('Diakrino Server instanciado')
    
    def initialize(self):
        '''
        Método para inicializar la instancia del engine
        '''
        #Cargamos el model manager
        self.model_manager.initialize()
        
        #Refrescamos el status de la instancia
        self.status = self.model_manager.getStatus()
        
        #Cargamos el analysis manager
        self.analysis_manager.initialize()
        
    
    def getStatus(self):
        '''
        Método para obtención del estatus de la instancia del engine
        '''
        return self.status
    
    def getLoadedMetadataModels(self):
        '''
        Método para entregar un listado de los models que se encuentran cargados en la instancia del motor
        '''
        #Verificamos que el estado actual si permita atender esta solicitud
        if self.status != EngineStatus.LISTO:
            return {}
        
        #Construimos los pares de id, nombre del modelo
        result = {}
        models = self.model_manager.getModels()
        
        for key in models:
            result[key] = models[key].get_nombre()
        
        return result
    
    def getModel(self,model_id):
        '''
        Proxy method to load an existing metadata model
        '''
        #Check the input
        if model_id is None:
            return None
        
        self.logger.info('Model request received with model id: '+str(model_id))
       
        #Check for the current status of the server engine.
        if self.status != EngineStatus.LISTO:
            return {}
        
        #Finally attempt to return the result of the query
        return self.model_manager.getModel(model_id)
    
    def getAnalysisDataSet(self,dataSetID):
        
        #Check for the instance of the analysis manager
        if self.analysis_manager is None:
            return None
        
        #Attempt to send the data set
        return self.analysis_manager.getDataSet(dataSetID)
    
    def getCurrentAnalysisDataSets(self):
        #Retrieve the data sets that have been loaded with the Analysis Manager
        return self.analysis_manager.getCurrentDataSets()
        
        