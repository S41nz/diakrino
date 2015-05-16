# -*- coding: latin-1 -*-
'''

Base Loader implementation that parses Candidate data collected from GoogleSheets
Created on 16/04/2015

@author: S41nz
'''

from model.loaders.base.base_loader import BaseLoader
from model.candidato import Candidato
from model.perfil_basico import PerfilBasico
from model.perfil_partido import PerfilPartido
from model.perfil_academico import PerfilAcademico

import gdata.spreadsheet.service

class GooglesheetsCandidatoModelLoader(BaseLoader):
    '''
    Attributes
    '''

    def __init__(self,id_seed):
        '''
        Constructor
        '''
        #Assignt the ID prefix for the models to be generated
        if id_seed is not None:
            self.id_seed = id_seed
    
    def loadModel(self, input_data):
        '''
        Method implementation that populates a Candidate instance our of a Google sheets
        data
        '''
        
        #Define the result set
        loadedModels = []
        
        #Check for input existence
        if input_data is None:
            return []
        
        entryNum = 0
        #If the data is valid then start parsint it and instantiating the models
        for entry in input_data:
            #Create the new model instance
            new_id = ""
            if self.id_seed is not None:
                new_id = new_id + self.id_seed+"_"
            new_id = new_id+"CANDIDATO_"+str(entryNum)
            
            newCandidato = Candidato(new_id)
            #Create the basic profile for that candidate
            newBasicProfile = PerfilBasico(new_id+"_PBASICO")
            
            for key in entry.custom:  
                if key == 'nombre':
                    print 'Candidate name received from the collector '+ str(entry.custom[key].text)
                    newBasicProfile.set_nombre(entry.custom[key].text)
                elif key == 'fecha de nacimiento':
                    newBasicProfile.set_fecha_de_nacimiento(entry.custom[key].text)
                elif key == 'partido':
                    #Crete a new party profile
                    newPartido = PerfilPartido(new_id+"_PPARTIDO")
                    newPartido.set_siglas(entry.custom[key].text)
                    newCandidato.set_perfil_partido(newPartido)
                elif key == 'estado civil':
                    newBasicProfile.set_estado_civil(entry.custom[key].text)
                elif key == 'maximo grado de estudios':
                    #Create a new academic profile
                    newAcademicProfile = PerfilAcademico(new_id+"_PACADEMICO")
                    newAcademicProfile.set_grado_actual(entry.custom[key].text)
                    newCandidato.set_perfil_academico(newAcademicProfile)
                elif key == 'url de imagen':
                    newBasicProfile.set_ruta_imagen(entry.custom[key].text)
                elif key == 'reseña':
                    newBasicProfile.set_resena(entry.custom[key].text)
                
                #Finally we add the basic profile into the candidate instance
                newCandidato.set_perfil_basico(newBasicProfile)
                
            #Add the instance to the list
            loadedModels.append(newCandidato)
                
            entryNum = entryNum+1
        
        
        return loadedModels
        
        