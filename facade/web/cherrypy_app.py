'''
Wrapper app to launch the Flask-based facade for Diakrino
Created on 26/04/2015

@author: S41nz
'''
from cherrypy import wsgiserver
from diakrino_flask import app

diakrinoDispatcher = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('45.33.6.16', 8080), diakrinoDispatcher)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()