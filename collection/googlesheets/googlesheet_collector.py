# -*- coding: latin-1 -*-
'''
Implementación de BaseCollector para recolectar registros específicos de una Google Spreadsheet
Created on 21/03/2015

@author: S41inz
'''
from collection.base.base_collector import  BaseCollector
from collection.enums.coleccion_status import ColeccionStatus

import gdata.spreadsheet.service



class GoogleSheetsCollector(BaseCollector):
    
    '''
    Atributos necesarios para el colector
    '''
    #Parámetros de entrada
    googleDataClient = ""
    
    #Llave de acceso para una spreadsheet específica
    curr_key = ""
    
    #ID de una hoja de trabajo específica de una spreadhseet
    curr_wksht_id = ""
    
    #Consulta para elegir un sub conjunto de datos determinado dentro del contenido de la spreadsheet
    curr_query = None
    
    #Resultado de la colección
    resultData = []
    
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.collectorParams = params
        
        #Establecemos el estado inicial del colector
        self.collectionStatus = ColeccionStatus.CREADO
        
        

    def initialize(self):
        #Llamamos al método de la clase padre
        BaseCollector.initialize(self)
        #Inicializamos el colector para la conexión con la google spreadseeht
        self.googleDataClient = gdata.spreadsheet.service.SpreadsheetsService()
        #Establecemos los datos de autenticación para el acceso a los datos
        self.googleDataClient.email = self.collectorParams['username']
        self.googleDataClient.password = self.collectorParams['password']
        self.googleDataClient.source = self.collectorParams['source_id']
        
        #Default a login programático
        self.googleDataClient.ProgrammaticLogin()
        
        if self.collectorParams.has_key('spreadsheet_key'):
            self.curr_key = self.collectorParams['spreadsheet_key']
        if self.collectorParams.has_key('worksheet_id'):
            self.curr_wksht_id = self.collectorParams['worksheet_id']
        
        #Reseteamos los datos de resultados
        self.resultData = None
        
        #Establecemos el estado como inicializado
        self.collectionStatus = ColeccionStatus.LISTO

    def collect(self):
        BaseCollector.collect(self)
        #Notificamos que estamos colectando
        self.collectionStatus = ColeccionStatus.COLECTANDO
        
        #Garantizamos que se tengan los datos necesarios para acceder al dataset
        if self.collectionOptions.has_key('spreadsheet_key'):
            self.curr_key = self.collectionOptions['spreadsheet_key']
        if self.collectionOptions.has_key('worksheet_id'):
            self.curr_wksht_id = self.collectionOptions['worksheet_id']
        if self.collectionOptions.has_key('query'):
            self.curr_query = self.collectionOptions['query']
        #Obtenemos los datos de la Google Data API
        
        self.resultData = self.googleDataClient.GetListFeed(self.curr_key, self.curr_wksht_id)
        
        #Filtramos los datos si es necesario
        self.filterData()
        
        #Notificamos que hemos terminado la collección
        self.collectionStatus = ColeccionStatus.EXITO

    def filterData(self):
        #Preparamos la lista para los resultados filtrados
        filteredResult = []
        
        #Primero nos aseguramos de que haya algo que filtrar
        if self.collectionOptions.has_key('keycolumn_id') and self.collectionOptions.has_key('search_term'):
            column_id = self.collectionOptions['keycolumn_id']
            search_term = self.collectionOptions['search_term']

            for i, entry in enumerate(self.resultData.entry):
                print entry
                if isinstance(self.resultData, gdata.spreadsheet.SpreadsheetsListFeed):
                    for key in entry.custom:
                        if key == column_id and entry.custom[key].text == search_term: 
                            #Encontramos nuestra entrada dentro del dataset
                            filteredResult.append(entry)
                
                    
         
        
            #Despues del filtrado asignamos el resultado final
            self.resultData = filteredResult

        
    def printResult(self, feed):
        for i, entry in enumerate(feed.entry):
            if isinstance(feed, gdata.spreadsheet.SpreadsheetsCellsFeed):
                print '%s %s\n' % (entry.title.text, entry.content.text)
            elif isinstance(feed, gdata.spreadsheet.SpreadsheetsListFeed):
                print '%s %s %s' % (i, entry.title.text, entry.content.text)
                # Print this row's value for each column (the custom dictionary is
                # built using the gsx: elements in the entry.)
                print 'Contents:'
                for key in entry.custom:  
                    print '  %s: %s' % (key, entry.custom[key].text) 
                    print '\n',
            else:
                print '%s %s\n' % (i, entry.title.text)
        

    def setCollectionOptions(self, options):
        self.collectionOptions = BaseCollector.setCollectionOptions(self, options)
        self.collectionOptions = options
        

    def getSupportedCollectionOptions(self):
        self.supportedCollectionOptions = BaseCollector.getSupportedCollectionOptions(self)
        
        self.supportedCollectionOptions = ['spreadsheet_key','worksheet_id','keycolumn_id','search_term']
        
        return self.supportedCollectionOptions
    


    def getData(self):
        BaseCollector.getData(self)
        return self.resultData


    def getStatus(self):
        return BaseCollector.getStatus(self)

        
        