from msilib.schema import Property
from os import system
import string
import time
from clases.libro import Libro

class Ejemplar(Libro):
    __numeroDeEjemplares = 0

    def __init__(self, nombre: string, autor: string, paginas: int) -> None:
        super().__init__(nombre, autor, paginas)

    @property
    def NumeroDeEjemplares(self) -> int:
        return self.__numeroDeEjemplares

    def AgregarEjemplar(self, cantidad: int) -> None:
        self.__numeroDeEjemplares += cantidad

    def RestarEjemplar(self, cantidad: int) -> None:
        if(cantidad <= self.NumeroDeEjemplares):
            self.__numeroDeEjemplares -= cantidad
        else:
            system('cls')
            print('no se pueden eliminar mas ejemplares de los que hay')
            time.sleep(2)