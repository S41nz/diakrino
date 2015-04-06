'''

Fachada en flask para montar una API de webservice para consumo de diakrinos
Created on 06/04/2015

@author: S41nz
'''

import os
from flask import Flask
from flask import request

app = Flask(__name__)
#add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

#Mensage de prueba
@app.route("/test")
def test():
    return "<strong>Esta es una prueba</strong>"
    
#Mensaje de bienvenida para el motor desde esta facahda
@app.route("/")
def hello():
    return "Hola desde Diakino"

if __name__ == "__main__":
    app.run()

