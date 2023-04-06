import math
from tokenize import Double

class Punto:
    __X = 0
    __Y = 0

    def __init__(self, x:float, y:float) -> None:
        self.nombre = "Punto"
        self.__X = (x, self.__X)[x == '']
        self.__Y = (x, self.__Y)[y == '']
        self.__coordenadas = (self.__X,self.__Y)

    @property
    def x(self):
        return self.__X

    @property
    def y(self):
        return self.__Y

    @property
    def Coordenadas(self):
        return self.__coordenadas

    def calcularDistanciaDesde(self, punto: "Punto") -> float: 
            # print(f'{self.Coordenadas} -- {punto.Coordenadas}')

            return math.dist(self.Coordenadas,punto.Coordenadas)
