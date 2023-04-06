
from clases.motor import Motor
import string


class Auto:

    __averias = []
    __motor: Motor

    def __init__(self, marca: string, modelo: string, motor: Motor) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor

    def Marca(self) -> string:
        return self.__marca
    
    def Modelo(self) -> string:
        return self.__modelo

    def Motor(self) -> Motor:
        return self.__motor
    
    def PrecioAverias(self) -> float:
        costo = 0
        for i in self.__averias:
            costo += i[0]

        return costo
    
    def DetalleDeAverias(self) -> None:
        for i in self.__averias:
            print(f'averia: {i[1]}, costo: {i[0]}')
    
    def SumaAverias(self, averia: list) -> None:
        self.__averias.append(averia) 
        if(averia[1] == 'aceite') or (averia[1] == 'Aceite'):
            self.__motor.AgregarLitrosAceite(10)