from Empleado import Empleado


class Maestro(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion):
        Empleado.__init__(self, id, n1, n2, a1, a2, dir, nEmp)
        self.__facultad = facultad
        self.__especializacion = especializacion

    # def __str__(self):
    #     return Empleado.__str__(self, True) + f'\r\nMaestro : {self.__facultad} {self.__especializacion} '

    def __str__(self):
        return Empleado.__str__(self) + f'\r\nMaestro : {self.__facultad} {self.__especializacion} '

    def getTipo(self):
        return "Maestro"
