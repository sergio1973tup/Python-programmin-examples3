

from os import system
import time
from clases.ejemplar import Ejemplar
from clases.libro import Libro


class Controlador:
    __ejemplares = []

    def NuevoLibro(self) -> Libro:
        system('cls')
        nombre = input('Ingrse nombre del libro: ')
        autor = input('Ingrse el autor: ')
        paginas = input('Ingrese la cantidad de paginas: ')
        
        self.__ejemplares.append(Ejemplar(nombre,autor,paginas))
        self.__ejemplares[len(self.__ejemplares)-1].AgregarEjemplar(1)
        system('cls')
        print('Ha ingresado un nuevo libro a la biblioteca, sera el primer ejemplar disponible')
        time.sleep(2)

    def NuevoEjemplar(self) -> None:
        if(len(self.__ejemplares) > 0):
            self.__ejemplares[self.SeleccionarLibro()-1].AgregarEjemplar(int(input('cuantos desea agregar: ')))
        else: 
            system('cls')
            print('No hay libros disponibles')
            time.sleep(2)
        
    def EliminarEjemplar(self) -> None:
        if(len(self.__ejemplares) > 0):
            libroSeleccionado =  self.SeleccionarLibro()
            cantidad = int(input('cuantos desea eliminar: '))
            if(self.__ejemplares[libroSeleccionado-1].NumeroDeEjemplares == cantidad):
                print('Al aliminar todos los ejemplares se eliminara el libro de la bibiloteca ')
                time.sleep(1)
                self.__ejemplares.pop(libroSeleccionado-1)
            else:
                self.__ejemplares[libroSeleccionado-1].RestarEjemplar(cantidad)
        else:
            system('cls')
            print('No hay libros disponibles')
            time.sleep(2)

    def MostrarLibros(self) -> None:
        if(len(self.__ejemplares) > 0):
            system('cls')
            count = 1
            for i in self.__ejemplares:
                print(f'{count} - Nombre: {i.Nombre} - Autor: {i.Autor} - Paginas: {i.Paginas} - Ejemplares disponibles: {i.NumeroDeEjemplares}')
                count = count+1
        else: 
            system('cls')
            print('No hay libros disponibles')
            time.sleep(2)

    def SeleccionarLibro(self) -> int:
        libroSeleccionado = 0
        while(libroSeleccionado > len(self.__ejemplares)) or (libroSeleccionado <= 0):
            self.MostrarLibros()
            libroSeleccionado = int(input('Seleccione el numero de libro: '))
            
        return libroSeleccionado