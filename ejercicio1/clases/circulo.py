from clases.punto import Punto
import math

class Circulo:
    __radio = float

    def __init__(self, centro: Punto, radio: float) -> None:
        self.__radio = radio
        self.__Centro = centro
    
    @property
    def radio(self) -> float:
        return self.__radio
    
    @property
    def centro(self) -> Punto:
        return self.__Centro

    @property
    def Area(self):
        return (math.pi * pow(self.radio,2))

    @property
    def Perimetro(self):
        return (2 * math.pi * self.radio)