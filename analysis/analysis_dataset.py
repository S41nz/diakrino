'''
Class that defines a given Data set to store the result of a given analysis process

@author: psainza
'''

from analysis.enums.dataset_status import DataSetStatus

class AnalysisDataSet:
    '''
    Attributes
    '''

    def __init__(self,dataSetID,dataSetType):
        '''
        Constructor
        '''
        #Define the data set ID
        self.dataSetID = dataSetID
        
        #Define the data set type
        self.dataSetType = dataSetType
        
        #Initialize the dataset status
        self.status = DataSetStatus.EMPTY

    def get_status(self):
        return self.status


    def set_status(self, value):
        self.status = value


    def get_data_set_id(self):
        return self.dataSetID


    def get_data_set_type(self):
        return self.dataSetType


    def get_data_set_status(self):
        return self.dataSetStatus


    def get_data(self):
        return self.data


    def set_data_set_status(self, value):
        self.dataSetStatus = value


    def set_data(self, value):
        self.data = value

        