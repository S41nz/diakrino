'''
Enumeration class that defines the type of data sets that contain results from data analysis in terms of its persistence

@author: S41nz
'''

class DataSetType:
    #Enumeration values
    
    #The data set is cacheable
    CACHEABLE = 0
    #The data set is feed on streaming
    STREAMING = 1
    #The data set requires direct fetch from its source
    DIRECT_FETCH = 2
        