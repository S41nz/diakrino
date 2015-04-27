'''
Manager entity to launch, coordinate and notify all the results from data analysis tasks that could be involved for a given
electoral process
Created on 26/04/2015

@author: S41nz
'''
from engine.enums.engine_status import EngineStatus
from model.enums.categoria_cuenta import CategoriaCuenta
from collection.rawfiles.csv_collector import CSVCollector
from collection.enums.coleccion_status import ColeccionStatus

import logging

class AnalysisManager:
    '''
    Attributes
    '''
    resultDataSets = {}


    def __init__(self):
        '''
        Constructor
        '''
        #Creamos el logger correspondiente del manager del modelo
        self.logger = logging.getLogger("AnalysisManager") 
        self.status = EngineStatus.CREADO
        
    def initialize(self):
        #Load each data set to start serving
        self.refreshResultDataSet()
        
        self.status = EngineStatus.LISTO
        
    def refreshResultDataSet(self):
        #Clean the dictionary
        self.resultDataSets = {}
        
        #Load GDL candidates
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/AlfonsoPetersen.csv', '2015.gdl.alfonso_petersen.twitter.followers')
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/rvillanueval.csv', '2015.gdl.ricardo_villanueva.twitter.followers')
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/EnriqueAlfaroR.csv', '2015.gdl.enrique_alfaro.twitter.followers')
        
        
    def loadDataSet(self,fileName,dataSetID):
        #Create the collection params
        collectorParams = {'file_path':fileName}
        #Instantiate the collector
        analysisCollector = CSVCollector(collectorParams)
        
        #Check for correct creation
        if analysisCollector.getStatus() != ColeccionStatus.CREADO:
            return
        
        #Initialize
        analysisCollector.initialize()
        
        #Check for correct initialization
        if analysisCollector.getStatus() != ColeccionStatus.LISTO:
            return
        
        #Collect the data
        analysisCollector.collect()
        
        #Check for collection result
        if analysisCollector.getStatus() == ColeccionStatus.EXITO:
            self.resultDataSets[dataSetID] = analysisCollector.getData()
    
        self.logger.info('Analysis data for data set ID: '+dataSetID+' has been completed')
    
    
    def getDataSet(self,dataSetID):
        #Check first for the received dataSet ID
        if dataSetID is None:
            return None
        elif dataSetID is not None:
            return self.resultDataSets[dataSetID]
        
    def getCurrentDataSets(self):
            return self.resultDataSets.keys()