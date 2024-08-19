from modules.Plist import * # Importamos la clase Lista y todos sus métodos
from datetime import datetime # Importamos la función datetime.datetime
from random import choice # Importamos especificamente la función random.choice

# Lista de listas con nombres de personas
listas = [['ramirez', 'perez', 'sanchez', 'torres', 'martinez'],
          ['jose', 'miguel', 'carlos', 'juan', 'ramiro', 'luis'],
          ['molina', 'santiago', 'garcia', 'ochoa', 'hernandez', 'solano']]

# Creamos una instancia de la clase Lista con un nombre aleatorio de la lista de listas y la fecha actual
lista = Lista(choice(listas), datetime.now().strftime('%Y-%m-%d'), listas[randint(0, len(listas) - 1)][randint(0, len(listas[0]) - 1)]) 
while True: # bucle infinito para que el programa no se detenga
    try:
        # Impresion de opciones de interaccion y captura de la opcion
        opcion = int(input('Seleccione una accion a realizar:\n1. Agregar un nombre a la lista\n2. Eliminar un nombre de la lista\
                            \n3. Mostrar la lista actual\n4. Salir del programa\n\nIntrodusca su opcion: '))
        
        if opcion == 1: # Escribir un nombre en la lista
            print(lista.write())
            
        elif opcion == 2: # Eliminar un nombre de la lista
            print(lista.rewrite())
            
        elif opcion == 3: # Mostrar la lista actual
            print(lista.read())
            
        elif opcion == 4: # Salir del programa
            exit()
        
        else: # Manejo de opciones no validas
            print('Error: Opcion no valida.\n')
                
    except ValueError: # Manejo por valores no numericos
        print('Error: Ingreso de valor no numerico.\n')