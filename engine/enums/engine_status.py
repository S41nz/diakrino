# -*- coding: latin-1 -*-
'''
Enumeración que define los estados posibles de una instancia de un engine o manager determinado
Created on 12/04/2015

@author: S41nz
'''

class EngineStatus:
    #Enumeraciones
    #Estado para definir que apenas se creó la instancia de 
    CREADO = "Creado" 
    #Este estado debe de establecerse después de completar la inicialización de la instancia
    LISTO = "Listo"
    #Estado para notificar que se está procesando una solicitud determinada
    PROCESANDO = "Procesando"
    #Estado para notificar que la ejecución de la tarea fue un éxito
    EXITO = "Éxito"
    #Estado para notificar que se terminó una tarea determinada con errores
    ERROR = "Error"
    #Estado para notificar que se terminó una tarea determinada con advertencias (errores no graves)
    ADVERTENCIA = "Advertencia"
