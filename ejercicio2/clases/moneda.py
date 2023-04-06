from os import system
import string

class Moneda:

    def __init__(self, Iso: string, nombre: string, simbolo: string) -> None:
        self.__iso = Iso
        self.__nombre = nombre
        self.__simbolo = simbolo

    @property
    def CodigoISO(self) -> string:
        return self.__iso

    @property
    def Nombre(self) -> string:
        return self.__nombre

    @property
    def Simbolo(self) -> string:
        return self.__simbolo