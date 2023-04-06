from msilib.schema import Property
import string


class Libro:
    __nombre = ''
    __autor = ''
    __paginas = 0

    def __init__(self, nombre: string, autor: string, paginas: int) -> None:
        self.__nombre = (nombre,self.__nombre)[nombre == '']
        self.__autor = (autor,self.__autor)[autor == '']
        self.__paginas = (paginas,self.__paginas)[paginas == '']

    @property
    def Nombre(self) -> string:
        return self.__nombre
    
    @property
    def Autor(self) -> string:
        return self.__autor

    @property
    def Paginas(self) -> int:
        return self.__paginas