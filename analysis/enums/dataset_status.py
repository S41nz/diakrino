'''
Enumeration created to communicate which is the current status of a given dataset

@author: psainza
'''

class DataSetStatus:
    
    #Initial state of the data set
    EMPTY = 0
    
    #When the data set is being filled with the data
    LOADING = 1
    
    #When the data loading is completed and data is ready for consumption
    REFRESHED = 2
    
    #Status applicable only to streaming datasets, indicating that they are already streaming
    STREAMING_STARTED = 3
    
    #Status applicable only to streaming datasets, indicating that the streaming has finished
    STREAMING_ENDED = 4
    
    #Status indicating that some error happened at a given stage of the dataset lifecycle
    ERROR = 5
    
    