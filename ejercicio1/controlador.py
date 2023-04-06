from clases import Punto,Circulo,Triangulo

class ControladoFachada:
    def __init__(self) -> None:
        pass

    def crearCirculo(Self, px: float, py: float, radio: float) -> Circulo:
        return Circulo(Punto(px,py), radio)

    def calcularAreaCirculo(Self, circulo: Circulo) -> float:
        return circulo.Area

    def calcularPerimetroCirculo(Self, circulo: Circulo) -> float:
        return circulo.Perimetro

    def punto(Self) -> Punto:
        print('Coordenasdas del Punto ')
        return Punto(int(input('ingrese coord. x: ')),int(input('ingrese coord. y: ')))

    def crearTriangulo(Self, p1: "punto", p2: "punto", p3: "punto" ) -> Triangulo:
        return Triangulo(p1,p2,p3)

    def calcularAreaTriangulo(Self, triangulo: "crearTriangulo") -> float:
        return triangulo.Area

    def calcularPerimetroTriangulo(Self, triangulo: Triangulo) -> float:
        return triangulo.perimetro