# -*- coding: latin-1 -*-
'''
Enumeración para determinar los tipos posibles en los que se puede encontrar un colector

@author: SA1nz
'''

class ColeccionStatus:

     #Enumeraciones
     #Estado para definir que apenas se creó la instancia de 
    CREADO = "Creado" 
    #Este estado debe de establecerse despues de completar la llamada a initialize()
    LISTO = "Listo"
    #Estado para notificar que se esta colectando, durante la llamada de collect()
    COLECTANDO = "Colectando"
    #Estado para notificar que la colección de datos tuvo éxito
    EXITO = "Terminado con éxito"
    #Estado para notificar que se terminó la colección con errores
    ERROR = "Terminado con errores"
    #Estado para notificar que se terminó la colección con advertencias (errores no graves)
    ADVERTENCIA = "Terminado con advertencias"
    

