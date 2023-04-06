

class Motor:
    __litros_aceite = 10
    __hp: int

    def __init__(self, hp: int) -> None:
        self.__hp = hp

    def Hp(self) -> int:
        return self.__hp

    def LitrosAceite(self) -> int:
        return self.__litros_aceite

    def AgregarLitrosAceite(self, litros: int) -> None:
        self.__litros_aceite += litros