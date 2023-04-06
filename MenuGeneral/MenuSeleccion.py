

from os import system
import string


class MenuDeSeleccion:
    __titulo: string
    __opciones: list

    def __init__(self, titulo: string , opciones: list) -> str:
        self.__titulo = titulo
        self.__opciones = opciones

    def seleccion(self) -> int:
        system('cls')
        print(self.__titulo)
        for i in self.__opciones:
            print(f'{i}: ')

        return input('selecciones una opcion: ')