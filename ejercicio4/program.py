import sys
import time

from controlador import Controlador
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion

class Program:
    opciones = ['1-CREAR LIBRO','2-AGREGAR EJEMPLAR','3-ELIMINAR EJEMPLAR','4-MOSTRAR LIBROS','5-SALIR']
    menuPrincipal = MenuDeSeleccion('Menu Pricipal',opciones)
    controladorGeneral = Controlador()

    
    seleccion = ''

    while(seleccion != str(len(opciones))):
        seleccion = menuPrincipal.seleccion()

        if(seleccion == '1'):
            controladorGeneral.NuevoLibro()
        if(seleccion == '2'):
            controladorGeneral.NuevoEjemplar()
        if(seleccion == '3'):
            controladorGeneral.EliminarEjemplar()
        if(seleccion == '4'):
            controladorGeneral.MostrarLibros()
            time.sleep(3)
