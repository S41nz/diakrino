'''

Fachada en flask para montar una API de webservice para consumo de diakrinos
Created on 06/04/2015

@author: S41nz
'''
from engine.diakrino_server import DiakrinoServer

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

if __name__ == "__main__":
    app.run()

