from Persona import Persona


class Visitante(Persona):
    def __init__(self, n1, n2, a1, a2, dir, razon, edificio, id):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__razon = razon
        self.__edificio = edificio

    def __str__(self):
        return super().__str__() + f'\n\rVisitante : {self.__razon} {self.__edificio} '
