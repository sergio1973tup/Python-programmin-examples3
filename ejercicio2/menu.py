from os import system
import sys
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion
from controlador import ControladorDeFachada

class Menu:

    opciones = ['1-CREAR CUENTA', '2-ELIMINAR CUENTA','3-SELECCIONAR CUENTA','4-SALIR']
    operaciones = ['1-DEPOSITAR','2-EXTRAER','3-CONSULTA DE SALDOS','4-SALIR']
    controlador = ControladorDeFachada()
    seleccion = ''
    menuOpciones = MenuDeSeleccion('Menu Principal',opciones)
    menuOperaciones = MenuDeSeleccion('Menu Operaciones', operaciones)

    while(seleccion != str(len(opciones))):

        seleccion = menuOpciones.seleccion()

        if(seleccion == '1'):
            controlador.CrearCuentas()
        
        elif(seleccion == '2'):
            controlador.EliminarCuenta(controlador.SeleccionCuenta())
            

        elif(seleccion == '3'):
            cuentaSeleccionada = controlador.SeleccionCuenta()
            if((cuentaSeleccionada != 0) & (cuentaSeleccionada <= len(controlador.cuentas))):
                operacion = ''
                
                while(operacion != str(len(operaciones))): 
                    
                    operacion = menuOperaciones.seleccion()
                    if(operacion == '1'): 
                        controlador.Depositar(cuentaSeleccionada)
                    elif(operacion == '2'):
                        controlador.Extraer(cuentaSeleccionada)
                    elif(operacion == '3'):
                        controlador.Disponibles(cuentaSeleccionada)

