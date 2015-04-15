'''
Abstract class that defines the functionality to load a given model class from a given collected dataset

Created on 14/04/2015

@author: S41nz 
'''
from abc import  ABCMeta, abstractmethod

class BaseLoader:
    __metaclass__ = ABCMeta
    '''
    Attributes
    '''
    
    @abstractmethod
    def loadModel(self,input_data):
        return None    