import string
from clases.moneda import Moneda

class Cuenta:

    def __init__(self, moneda: Moneda) -> None:
        self.__saldo = 0
        self.__moneda = moneda

    def Saldo(self) -> float:
        return self.__saldo

    def Moneda(self) -> string:
        return self.__moneda

    def AcreditarSaldo(self, deposito: float) -> None:
        self.__saldo = self.__saldo + deposito

    def DebitarSaldo(self, extraccion: float) -> bool:
        if(self.__saldo >= extraccion):
            self.__saldo = self.__saldo - extraccion
            return True
        else:
            return False
