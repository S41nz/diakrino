'''
Wrapper app to launch the Flask-based facade for Diakrino
Created on 26/04/2015

@author: S41nz
'''
from cherrypy import wsgiserver
from diakrino_flask import app
import os

diakrinoDispatcher = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer((os.environ['DIAKRINO_HOSTNAME'], int(os.environ['DIAKRINO_PORT'])), diakrinoDispatcher)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()