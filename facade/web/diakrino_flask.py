'''

Fachada en flask para montar una API de webservice para consumo de diakrinos
Created on 06/04/2015

@author: S41nz
'''
from engine.diakrino_server import DiakrinoServer
from engine.enums.engine_status import EngineStatus
from analysis.analysis_dataset import AnalysisDataSet
from model.proceso_electoral import ProcesoElectoral
from model.entidad import Entidad
from model.candidato import Candidato
from model.perfil_basico import PerfilBasico

import os
import json
from flask import Flask
from flask import request
from bson import json_util

app = Flask(__name__)
#add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True
#Create the instance of the Diakrino Server
diakrinoServer = DiakrinoServer()
diakrinoServer.initialize()

'''
Handshake API
'''
#Mensage de prueba
@app.route("/test")
def test():
    return "<strong>Esta es una prueba</strong>"
    
#Mensaje de bienvenida para el motor desde esta facahda
@app.route("/")
def hello():
    return "Hola desde Diakino"

'''
API for Metadata Support
'''
@app.route("/diakrino/elections")
def getSupportedElectionProcesses():
    
    currentModels = diakrinoServer.getLoadedMetadataModels()
    
    #Check for None or emptyness
    if currentModels is None or len(currentModels.items()) == 0:
        #Notify the user that no models have been loaded
        return str(json.dumps('ERROR: There are no models loaded currently :-(',default=json_util.default))
    
    #Otherwise we send the list
    return str(json.dumps(currentModels.items(),default=json_util.default))

@app.route("/diakrino/<processID>/entities")
def getSupportedElectionEntities(processID):
    
    if processID is None:
        return str(json.dumps('ERROR: Invalid election process ID, please try again',default=json_util.default))
    
    electionModel = diakrinoServer.getModel(processID)
    
    #Check for a valid process ID
    if electionModel is None:
        return str(json.dumps('ERROR: Invalid election process ID, please try again',default=json_util.default))
    
    currentEntities = electionModel.get_entidades()
    
    if currentEntities is None or len(currentEntities) == 0:
        return str(json.dumps('No entities are assigned currently to this election process',default=json_util.default))
    
    result = {}
    #Capture the data into the result set
    for entity in currentEntities:
        result[entity.get_entidad_id()] = entity.get_nombre()
        
    #If we have meaningful data then we send it back
    return str(json.dumps(result,default=json_util.default))

@app.route("/diakrino/<processID>/<entityID>")
def getEntityMetadata(processID,entityID):
    #Check for Nones
    if processID is None:
        return str(json.dumps('ERROR: Invalid election process ID, please try again',default=json_util.default))
    if entityID is None:
        return str(json.dumps('ERROR: Invalid entity ID, please try again',default=json_util.default))
    
    electionModel = diakrinoServer.getModel(processID)
    
    #Check for a valid process ID
    if electionModel is None:
        return str(json.dumps('ERROR: Invalid election process ID, please try again',default=json_util.default))
    
    currentEntities = electionModel.get_entidades()
    
    if currentEntities is None or len(currentEntities) == 0:
        return str(json.dumps('No entities are assigned currently to this election process',default=json_util.default))
    
    #Check for ID existence within the entities
    entityMatch = None
    for loadedEntity in currentEntities:
        if entityID == loadedEntity.get_entidad_id():
            entityMatch = loadedEntity
            break
    
    if entityMatch is None:
        return str(json.dumps('ERROR: Invalid entity ID, please try again',default=json_util.default))
    
    #Otherwise we construct the result object and retrieve the result
    result = {}
    #ID
    result['id'] = entityMatch.get_entidad_id()
    #Name
    result['name'] = entityMatch.get_nombre()
    #Entity Type
    result['type'] = entityMatch.get_tipo_entidad()
    #Check for subentities if any
    subEntities = entityMatch.get_subentidades()
    #TODO: This needs to be a dictionary, not a list
    if subEntities is not None and len(subEntities) > 0:
        #Construct the list
        subEntityList = {}
        for subEntity in subEntities:
            subEntityList[subEntity.get_entidad_id()] = subEntity.get_nombre()
        #Just construct the directory with their immediate relationship
        result['subentities'] = subEntityList
    else:
        result['subentities'] = 'None'
    
    #Check for candidates if any
    candidates = entityMatch.get_candidatos()
    
    if candidates is not None and len(candidates) > 0:
        candidatesList = {}
        for candidate in candidates:
            candidatesList[candidate.get_id()] = candidate.get_perfil_basico().get_nombre()
        #Just construct the directory with their immediate relationship
        result['candidates'] = candidatesList
    else:
        result['candidates'] = 'None'
    
    #Send the result
    return str(json.dumps(result,default=json_util.default))
'''
API for Visualization Support
'''
@app.route("/diakrino/visual/candidates")
def getSupportedCandidates():
    #Extract the data sets
    currentDataSets = diakrinoServer.getCurrentAnalysisDataSets()
    supportedCandidates = []
    for dataSetID in currentDataSets:
        supportedCandidates.append(dataSetID.split('.')[2])
        
    #Transform the output to a JSON string
    return str(json.dumps({'supported_candidates':supportedCandidates},default=json_util.default))

@app.route("/diakrino/visual/twitter/followers/histogram/<candidateId>")
def getCandidateTwitterFollowersHistogram(candidateId):
    
    result = ""
    
    #Check for the received Candidate ID
    if candidateId is None:
        return str(json.dumps('Invalid candidate ID',default=json_util.default))
    
    #Check for the status of Analysis Manager
    #if diakrinoServer.getStatus() != EngineStatus.EXITO:
    #    return str(json.dumps('Not able to process the request :-( , try again later',default=json_util.default))
    
    #Construct the data set ID with the provided candidate name
    newDataSetID = '2015.gdl.'+candidateId+'.twitter.followers.histogram'
    
    #If valid then we proceed to query the data set to the analysis manager
    analysisDataSet = diakrinoServer.getAnalysisDataSet(newDataSetID)
    
    if analysisDataSet is None:
        return str(json.dumps('Invalid candidate ID',default=json_util.default))
    
    #Convert the results to JSON format
    result = str(json.dumps({'Candidate ID':candidateId,'Twitter followers histogram data':analysisDataSet.get_data()},default=json_util.default))
    
    return result

'''
API for Data Analysis Support
'''
@app.route("/diakrino/analysis/refresh/<password>")
def refreshAnalsysData(password):
    #Crapy  authentication in the meantime in order to prevent potential DoS attacks.
    
    #If parameter is None
    if password is None:
        return str(json.dumps('Not authorized to refresh',default=json_util.default))
    
    #If parameter is not correct
    if password != os.environ['DIAKRINO_ADMIN_PWD']:
        return str(json.dumps('Not authorized to refresh',default=json_util.default))
    
    #If the password is OK, then we refresh the analysis datasets
    diakrinoServer.refreshAnalysisData()
    
    return str(json.dumps('Analysis data cache refreshed :-)',default=json_util.default))

@app.route("/diakrino/metadata/refresh/<password>")
def refreshMetadataModel(password):
    #Crapy  authentication in the meantime in order to prevent potential DoS attacks.
    
    #If parameter is None
    if password is None:
        return str(json.dumps('Not authorized to refresh',default=json_util.default))
    
    #If parameter is not correct
    if password != os.environ['DIAKRINO_ADMIN_PWD']:
        return str(json.dumps('Not authorized to refresh',default=json_util.default))
    
    #If the password is OK, then we refresh the analysis datasets
    diakrinoServer.refreshMetadataModel()
    
    return str(json.dumps('Metadata model refreshed :-)',default=json_util.default))
    
if __name__ == "__main__":
    app.run()

