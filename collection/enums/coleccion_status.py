# -*- coding: latin-1 -*-
'''
Enumeraci�n para determinar los tipos posibles en los que se puede encontrar un colector

@author: SA1nz
'''

class ColeccionStatus:

     #Enumeraciones
     #Estado para definir que apenas se cre� la instancia de 
    CREADO = "Creado" 
    #Este estado debe de establecerse despues de completar la llamada a initialize()
    LISTO = "Listo"
    #Estado para notificar que se esta colectando, durante la llamada de collect()
    COLECTANDO = "Colectando"
    #Estado para notificar que la colecci�n de datos tuvo �xito
    EXITO = "Terminado con �xito"
    #Estado para notificar que se termin� la colecci�n con errores
    ERROR = "Terminado con errores"
    #Estado para notificar que se termin� la colecci�n con advertencias (errores no graves)
    ADVERTENCIA = "Terminado con advertencias"
    

