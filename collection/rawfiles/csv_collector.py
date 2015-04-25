'''
Collector class that parses the content of a CSV file.
Created on 25/04/2015

@author: S41nz
'''

from collection.base.base_collector import  BaseCollector
from collection.enums.coleccion_status import ColeccionStatus
import csv


class CSVCollector(BaseCollector):
    '''
    classdocs
    '''
    #File path to the CSV file
    file_path = ''
    
    

    def __init__(self, params):
        '''
        Constructor
        '''
        #Parse the initialization parameters
        self.collectorParams = params
        
        self.collectionStatus = ColeccionStatus.CREADO

    def initialize(self):
        BaseCollector.initialize(self)
        #Set the file path
        self.file_path = self.collectorParams['file_path']
        #initialize the result set
        self.result_data = None
        
        #Comunicate we are ready
        self.collectionStatus = ColeccionStatus.LISTO

    def collect(self):
        BaseCollector.collect(self)
        self.collectionStatus = ColeccionStatus.COLECTANDO
        
        #Check that we have a file path
        if self.file_path is not None:
            csvDataSource = open(self.file_path)
            #Parse the file
            self.result_data = csv.DictReader(csvDataSource)
            
        
        #Update the collection status
        self.collectionStatus = ColeccionStatus.EXITO

    def setCollectionOptions(self, options):
        self.collectionOptions =  BaseCollector.setCollectionOptions(self, options)
        self.collectionOptions = options

    def getSupportedCollectionOptions(self):
        self.supportedCollectionOptions = BaseCollector.getSupportedCollectionOptions(self)
        self.supportedCollectionOptions = ['file_path']
        return self.supportedCollectionOptions

    def getData(self):
        BaseCollector.getData(self)
        return self.result_data

    def getStatus(self):
        return BaseCollector.getStatus(self)

    def testPrint(self):
        for dataRow in self.result_data:
            print dataRow
        