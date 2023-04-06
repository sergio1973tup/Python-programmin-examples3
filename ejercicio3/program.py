
import sys

from controlador import Controlador
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion

class Program:
    opcionesPrincipales = ['1-CARGAR AUTO','2-GARAGE','3-SALIR']
    opcionesGarage = ['1-INGRESAR AUTO','2-CARGAR AVERIA','3-RETIRAR AUTO','4-SALIR']
    menuPricipal = MenuDeSeleccion('Menu Principal',opcionesPrincipales)
    menuGarage = MenuDeSeleccion('Menu Garage',opcionesGarage)
    controladorGeneral = Controlador()
    seleccion = ''

    while(seleccion != str(len(opcionesPrincipales))):

        seleccion = menuPricipal.seleccion()

        if(seleccion == '1'):
            controladorGeneral.CrearAuto()
        
        if(seleccion == '2'):
            opcion = ""
            while(opcion != str(len(opcionesGarage))):
                opcion = menuGarage.seleccion()
                if(opcion == '1'):
                    controladorGeneral.IngresarAuto()
                if(opcion == '2'):
                    controladorGeneral.CargarAveria()
                if(opcion == '3'):
                    controladorGeneral.RetirarAuto()