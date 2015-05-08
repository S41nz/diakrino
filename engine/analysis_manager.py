'''
Manager entity to launch, coordinate and notify all the results from data analysis tasks that could be involved for a given
electoral process
Created on 26/04/2015

@author: S41nz
'''
from engine.enums.engine_status import EngineStatus
from collection.rawfiles.csv_collector import CSVCollector
from collection.enums.coleccion_status import ColeccionStatus
from analysis.enums.dataset_type import DataSetType
from analysis.enums.dataset_status import DataSetStatus
from analysis.analysis_dataset import AnalysisDataSet

import logging

class AnalysisManager:
    '''
    Attributes
    '''
    #Collection containing all the cacheable datasets from the data analysis process
    dataSetsCache = {}
    
    #Directory that contains the references of the overall 
    analysisDataSets = {}


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
        self.analysisDataSets = {}
        
        #Load GDL candidates
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/AlfonsoPetersen.csv', '2015.gdl.alfonso_petersen.twitter.followers.histogram')
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/rvillanueval.csv', '2015.gdl.ricardo_villanueva.twitter.followers.histogram')
        self.loadDataSet('/diakrino_data/analysis/twitter/followers/EnriqueAlfaroR.csv', '2015.gdl.enrique_alfaro.twitter.followers.histogram')
        
        
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
        
        #Create the dataset, currently as Cacheable
        newDataSet = AnalysisDataSet(dataSetID,DataSetType.CACHEABLE)
        #Check for collection result
        if analysisCollector.getStatus() == ColeccionStatus.EXITO:
            fileData = analysisCollector.getData()
            rawDataSet = []
            newDataSet.set_data(rawDataSet)
            newDataSet.set_status(DataSetStatus.LOADING)
            #Create the image in memory for the file content
            for row in fileData:
                newDataSet.get_data().append(str(row))
                
            #Refresh the correct status as refreshed
            newDataSet.set_status(DataSetStatus.REFRESHED)
            self.analysisDataSets[dataSetID] = newDataSet
            
            #Also add the reference to the dataset cache
            self.dataSetsCache[dataSetID] = newDataSet
    
        self.logger.info('Analysis data for data set ID: '+dataSetID+' has been completed')
    
    
    def getDataSet(self,dataSetID):
        #Check first for the received dataSet ID
        if dataSetID is None:
            return None
        elif dataSetID is not None:
            #Check if the received key exists
            if dataSetID in self.getCurrentDataSets():
                return self.analysisDataSets[dataSetID]
            else:
                return None
        
    def getCurrentDataSets(self):
            return self.analysisDataSets.keys()