

import string
from clases.moneda import Moneda
from clases.cuenta import Cuenta


class Cuentas:

    def __init__(self, propietario: string) -> None:
        self.__Propietario = propietario
        self.__CuentaEnPesos = Cuenta(Moneda('ARS-032-2','Peso','$'))
        self.__CuentaEnDolares = Cuenta(Moneda('USN-997-2','Dolar','U$S'))

    @property
    def Propietario(self) -> string:
        return self.__Propietario

    @property
    def CuentaEnPesos(self) -> Cuenta:
        return self.__CuentaEnPesos

    @property
    def CuentaEnDolares(self) -> Cuenta:
        return self.__CuentaEnDolares