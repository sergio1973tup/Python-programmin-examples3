from abc import abstractmethod
from os import system
import sys
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion
import string
import time
from clases import cuentas
from clases import Moneda,Cuenta, Cuentas

class ControladorDeFachada:
    __cuentas = []

    @property
    def cuentas(self) -> list:
        return self.__cuentas

    def __init__(self) -> None:
        pass

    def CrearMoneda(self, nombre: string, ISO: string, simbolo: string) -> Moneda:
        return Moneda(ISO, nombre, simbolo)

    def CrearCuenta(self, moneda: Moneda, saldo: float) -> Cuenta:
        return Cuenta(moneda, saldo)

    def CrearCuentas(self) -> None:
        system('cls')
        self.cuentas.append(Cuentas(input('Ingrese el nombre del Propietario de la cuenta: ')))

    
    def SeleccionCuenta(self) -> int:
        cuentaSeleccionada = 0
        system('cls')
        if(len(self.cuentas)>0):
            self.MostrarCuentas()
                    
            cuentaSeleccionada = int(input('Seleccione la cuenta: '))
        else:
            print('No hay cuentas disponibles')
            time.sleep(3)

        return cuentaSeleccionada

    def MostrarCuentas(self) -> None:
            count = 0
            print('Cuentas Activas: ')
            for i in self.cuentas:
                print(f'{count+1} -- {i.Propietario}')
                count = count+1

    def EliminarCuenta(self, seleccion) -> None:
        if ((seleccion <= len(self.cuentas)) & (seleccion != 0)):
                    system('cls')
                    print(f'la cuenta de: {self.cuentas[seleccion-1].Propietario} fue eliminada')
                    self.cuentas.pop(seleccion-1)
                    time.sleep(3)
        elif((seleccion < 0)|(seleccion > len(self.cuentas))):
            print('La cuentas eleccionada no existe')
            time.sleep(3)

    def Depositar(self,cuentaSeleccionada) -> None:
        system('cls')
        self.Propietario(cuentaSeleccionada)

        divisa = self.SeleccionDeDivisa()
        if(divisa == 1):
            self.cuentas[cuentaSeleccionada-1].CuentaEnPesos.AcreditarSaldo(self.MontoElegido())
            self.SaldoActualPesos(cuentaSeleccionada)
        elif(divisa == 2):
            self.cuentas[cuentaSeleccionada-1].CuentaEnDolares.AcreditarSaldo(self.MontoElegido())
            self.SaldoActualDolares(cuentaSeleccionada)

    def Extraer(self, cuentaSeleccionada) -> None:
        system('cls')
        self.Propietario(cuentaSeleccionada)

        divisa = self.SeleccionDeDivisa()
        if(divisa == 1):
            if(self.cuentas[cuentaSeleccionada-1].CuentaEnPesos.DebitarSaldo(self.MontoElegido())):
                self.SaldoActualPesos(cuentaSeleccionada)
            else:
                self.SaldoInsuficiente(cuentaSeleccionada, divisa)
        elif(divisa == 2):
            if(self.cuentas[cuentaSeleccionada-1].CuentaEnDolares.DebitarSaldo(self.MontoElegido())):
                self.SaldoActualDolares(cuentaSeleccionada)
            else:
                self.SaldoInsuficiente(cuentaSeleccionada, divisa)

    def MontoElegido(self) -> float:
        return float(input('Ingrese el monto: '))

    def SeleccionDeDivisa(self) -> int:
        divisas = ['1-Pesos','2-Dolares']
        MenuDivisas = MenuDeSeleccion('Divisas Disponibles',divisas)
        
        return int(MenuDivisas.seleccion())

    def Disponibles(self, cuentaSeleccionada) -> None:
        system('cls')
        self.Propietario(cuentaSeleccionada)

        print(f'Saldo en Pesos: {self.cuentas[cuentaSeleccionada-1].CuentaEnPesos.Saldo()}')
        print(f'Saldo en Dolares: {self.cuentas[cuentaSeleccionada-1].CuentaEnDolares.Saldo()}')
        time.sleep(3)

    def SaldoActualPesos(self, cuentaSeleccionada ) -> None:
        print(f'Saldo actual en Pesos: {self.cuentas[cuentaSeleccionada-1].CuentaEnPesos.Saldo()}')
        time.sleep(3)

    def SaldoActualDolares(self, cuentaSeleccionada) -> None:
        print(f'Saldo actual en Dolares: {self.cuentas[cuentaSeleccionada-1].CuentaEnDolares.Saldo()}')
        time.sleep(3)

    def SaldoInsuficiente(self, cuentaSeleccionada, divisa) -> None:
        if(divisa == 1):
            print(f'Su saldo {self.cuentas[cuentaSeleccionada-1].CuentaEnPesos.Saldo()} es menor al que desea extraer ')
            time.sleep(3)
        else:
            print(f'Su saldo {self.cuentas[cuentaSeleccionada-1].CuentaEnDolares.Saldo()} es menor al que desea extraer ')
            time.sleep(3)

    def Propietario(self, cuentaSeleccionada) -> None:
        print(f'Cuenta de: {self.cuentas[cuentaSeleccionada-1].Propietario}')
        time.sleep(1)