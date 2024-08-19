from random import randint # Importamos la función random.randint

class Lista: 
    def __init__(self, nombres, fecha, encargado):
        # Atributos
        self.nombres = nombres 
        self.fecha = fecha
        self.encargado = encargado
    
    # Métodos
    def write(self): # Método para añadir un elemento a la lista
        nombres = ['Perez', 'Lopez', 'Rodriguez', 'Sanchez', 'Garcia',
                   'Martinez','Hernandez', 'Diaz', 'Perez', 'Lopez',
                   'Sanchez', 'Garcia', 'Martinez', 'Hernandez', 'Diaz']
        
        nombre = nombres[randint(1, len(nombres) -1)]
        self.nombres.append(nombre.capitalize())
        return f'Se ha añadido a {nombre.capitalize()} a la lista. Fecha: {self.fecha}.\n'
    
    def rewrite(self): # Método para eliminar un elemento de la lista
        return f'Se ha eliminado a {self.nombres.pop(randint(1, len(self.nombres) -1)).capitalize()} de la lista. Fecha: {self.fecha}.\n'
    
    def read(self): # Método para mostrar la lista actual, su encargado y la fecha actual
        return f'\n\nEncargado: {self.encargado.capitalize()}\t\t\tFecha: {self.fecha}\n\nLista: {', '.join(nombre.capitalize() for nombre in self.nombres)}\n'