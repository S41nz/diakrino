'''

Fachada en flask para montar una API de webservice para consumo de diakrinos
Created on 06/04/2015

@author: S41nz
'''
from engine.diakrino_server import DiakrinoServer
from engine.enums.engine_status import EngineStatus

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

#Mensage de prueba
@app.route("/test")
def test():
    return "<strong>Esta es una prueba</strong>"
    
#Mensaje de bienvenida para el motor desde esta facahda
@app.route("/")
def hello():
    return "Hola desde Diakino"

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
    
    #If we have a data set then we transform it to a readable output
    outputList = []
    for row in analysisDataSet:
        outputList.append(str(row))
    
    #Convert the results to JSON format
    result = str(json.dumps({'Candidate ID':candidateId,'Twitter Followers Histogram Data':outputList},default=json_util.default))
    
    return result

if __name__ == "__main__":
    app.run()

