# -*- coding: latin-1 -*-
'''
Enumeraci�n que define los estados posibles de una instancia de un engine o manager determinado
Created on 12/04/2015

@author: S41nz
'''

class EngineStatus:
    #Enumeraciones
    #Estado para definir que apenas se cre� la instancia de 
    CREADO = "Creado" 
    #Este estado debe de establecerse despu�s de completar la inicializaci�n de la instancia
    LISTO = "Listo"
    #Estado para notificar que se est� procesando una solicitud determinada
    PROCESANDO = "Procesando"
    #Estado para notificar que la ejecuci�n de la tarea fue un �xito
    EXITO = "�xito"
    #Estado para notificar que se termin� una tarea determinada con errores
    ERROR = "Error"
    #Estado para notificar que se termin� una tarea determinada con advertencias (errores no graves)
    ADVERTENCIA = "Advertencia"
