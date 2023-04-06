

import string
from xmlrpc.client import Boolean, boolean
from clases.motor import Motor
from clases import Auto


class Garage:

    __autos = 0
    __auto = Auto('','',Motor(0))

    def __init__(self) -> None:
        pass
    
    def AceptarAuto(self, auto: Auto) -> Boolean:
        if((auto.Marca() == '') or (auto.Modelo() == '')):
            return False
        else:
            self.__auto = auto
            self.__autos = self.__autos + 1
            return True

    def SacarAuto(self) -> None:
        self.__auto = Auto('','','')

    def AutosAtendidos(self) -> int:
        return self.__autos

    def Auto(self) -> Auto:
        return self.__auto

    def IncorporarAveria(self, precio: float, descripcion: string) -> boolean:
        if(precio > 0) & (descripcion != ''):
            nuevaAveria = [precio,descripcion] 
            self.__auto.SumaAverias(nuevaAveria)
            return True
        else:
            return False