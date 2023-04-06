
from os import system
from sqlite3 import Time
import time
from clases.garage import Garage
from clases.motor import Motor
from clases.auto import Auto
import sys
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion


class Controlador:
    __MyGarage = Garage()
    __auto = Auto('','', Motor(0))

    def CrearAuto(self) -> None:
        system('cls')
        marca = input('Ingrese la marca del auto: ')
        modelo = input('Ingrese el modelo del auto: ')
        HpMotor = int(input('Ingrese los HP del motor: '))
        NewMotor = Motor(HpMotor)
        
        self.__auto = Auto(marca,modelo,NewMotor)

    def IngresarAuto(self) -> None:
        if(self.__auto.Marca() == ''):
            print('No hay auto para ingresar en el Garage')
            time.sleep(2)
        else:
            if(self.__MyGarage.AceptarAuto(self.__auto)):
                system('cls')
                print('El Auto se encuentra en el Garage !!')
                time.sleep(3)
            else:
                print('Su Auto no fue aceptado, carguelo nuevamente')
                time.sleep(3)
        

    def CargarAveria(self) -> None:
        if(self.__MyGarage.Auto().Marca() == ''):
            print('No hay auto en el Garage')
            time.sleep(2)
        else:
            system('cls')
            descricpion = input('ingrese el la descripcion de averia: ')
            costo = int(input('ingrese el costo de la averia: '))

            if(self.__MyGarage.IncorporarAveria(costo,descricpion)):
                print('averia cargada')
                time.sleep(3)
            else:
                print('error en averia')
                time.sleep(3)

    def RetirarAuto(self) -> Auto:
        if(self.__MyGarage.Auto().Marca() == ''):
            print('No hay Auto en el Garage')
            time.sleep(2)
        else:
            system('cls')
            autoRetirado = self.__MyGarage.Auto()
            print(f'Se retira el auto: {autoRetirado.Marca()}')
            print(f'modelo: {autoRetirado.Modelo()}, HP motor: {autoRetirado.Motor().Hp()} ,litros de aceite: {autoRetirado.Motor().LitrosAceite()}')
            autoRetirado.DetalleDeAverias()
            print(f'Total en averias: {autoRetirado.PrecioAverias()}')
            print(f'Autos atendidos hasta el momento: {self.__MyGarage.AutosAtendidos()}')
            self.__MyGarage.SacarAuto()
            self.__auto = Auto('','','')
            time.sleep(6)