from os import system
import time
import sys
sys.path.append('..')
from MenuGeneral.MenuSeleccion import MenuDeSeleccion
from clases.circulo import Circulo
from clases.triangulo import Triangulo
from controlador import ControladoFachada

class Menu:

        opciones = ['1-CREAR CIRCULO','2-CREAR TRIANGULO','3-SALIR']
        menuPrincipal = MenuDeSeleccion('Menu Principal',opciones)
        calculos = ['1-CALCULAR AREA', '2-CALCULAR PERIMETRO','3-SALIR']
        menuCalculo = MenuDeSeleccion('Menu De Calculo',calculos)
        controlador = ControladoFachada()
        circuloCreado = Circulo
        trianguloCreado = Triangulo
        seleccion = ''

        while(seleccion != str(len(opciones))):
            
            seleccion = menuPrincipal.seleccion()
            if(seleccion == '1'):
                calculo = ''
                system('cls')

                circuloCreado = controlador.crearCirculo(int(input('Cordenada x: ')), int(input('Cordenada y: ')), int(input('Ingrese el radio del circulo: ')))
                while(calculo != str(len(calculos))):
                    
                    calculo = menuCalculo.seleccion()
                    if(calculo == '1'):
                        system('cls')
                        print(f'El Area del circulo es: {controlador.calcularAreaCirculo(circuloCreado)}')
                        time.sleep(3)
                    elif(calculo == '2'):
                        system('cls')
                        print(f'El Perimetro del circulo es: {controlador.calcularPerimetroCirculo(circuloCreado)}')
                        time.sleep(3)

            elif(seleccion == '2'):
                calculo = ''
                system('cls')

                trianguloCreado = controlador.crearTriangulo(controlador.punto(),controlador.punto(),controlador.punto())
                while(calculo != str(len(calculos))): 
                    
                    calculo = menuCalculo.seleccion()
                    if(calculo == '1'):
                        system('cls')
                        print(f'El Area del triangulo es: {controlador.calcularAreaTriangulo(trianguloCreado)}')
                        time.sleep(3)
                    elif(calculo == '2'):
                        system('cls')
                        print(f'El Perimetro del triangulo es: {controlador.calcularPerimetroTriangulo(trianguloCreado)}')
                        time.sleep(3)
        system('cls')