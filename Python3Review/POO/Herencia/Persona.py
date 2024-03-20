from abc import ABC, abstractmethod
# @abstractmethod
# def mover(self):
#     pass


class Persona(ABC):
    def __init__(self, id, n1, n2, a1, a2, dir):
        self.__id = id
        self.__n1 = n1
        self.__n2 = n2
        self.__a1 = a1
        self.__a2 = a2
        self.__dir = dir

    def getId(self):
        return self.__id

    def getN1(self):
        return self.__n1

    def getN2(self):
        return self.__n2

    def getA1(self):
        return self.__a1

    def getA2(self):
        return self.__a2

    def getDir(self):
        return self.__dir

    def __str__(self):
        return f'\r\nPersona : {self.getId()} {self.getN1()} {self.getN2()} {self.getA1()} {self.getA2()}'

    @abstractmethod
    def queComen(self):
        pass

# persona = Persona('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa')
# print(persona)