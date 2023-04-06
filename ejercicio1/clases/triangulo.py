from clases.punto import Punto
import math

class Triangulo:

    def __init__(self, punto_1: Punto, punto_2: Punto, punto_3: Punto) -> None:
        self.__Punto1 = punto_1
        self.__Punto2 = punto_2
        self.__Punto3 = punto_3

    @property
    def Punto_1(self) -> Punto:
        return self.__Punto1

    @property
    def Punto_2(self) -> Punto:
        return self.__Punto2

    @property
    def Punto_3(self) -> Punto:
        return self.__Punto3

    @property
    def Area(self) -> float:
        p1p2 = self.__Punto1.calcularDistanciaDesde(self.__Punto2)
        p1p3 = self.__Punto1.calcularDistanciaDesde(self.__Punto3)
        p2p3 = math.sqrt((pow(p1p2,2)+pow(p1p3,2)))
        semiperimetro = self.perimetro / 2
        return math.sqrt(semiperimetro * (semiperimetro - p1p2) * (semiperimetro - p1p3) * (semiperimetro - p2p3))

    @property
    def perimetro(self) -> float:
        p1p2 = self.__Punto1.calcularDistanciaDesde(self.__Punto2)
        p1p3 = self.__Punto1.calcularDistanciaDesde(self.__Punto3)
        p2p3 = math.sqrt((pow(p1p2,2)+pow(p1p3,2)))
        return  p1p2 + p1p3 + p2p3
