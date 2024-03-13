from Empleado import Empleado


class Administrativo(Empleado):
    # def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo):
    #     super().__init__(id, n1, n2, a1, a2, dir, nEmp)
    #     self.__area = area
    #     self.__campo = campo

    # def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
    #     super().__init__(id, n1, n2, a1, a2, dir, nEmp)

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area="", campo=""):
        super().__init__(id, n1, n2, a1, a2, dir, nEmp)
        self.__area = area
        self.__campo = campo

    def setCampo(self, campo):
        self.__campo = campo

    def getCampo(self):
        return self.__campo

    def setArea(self, area):
        self.__area = area

    def getArea(self):
        return self.__area

    # def __str__(self, mostrarEmpleado):
    #     return Empleado.__str__(self, mostrarEmpleado) + f"\n\rAdministrativo : {self.getCampo()} {self.getArea()} "

    def __str__(self):
        if type(self) is Administrativo:
            return Empleado.__str__(self) + f"\n\rAdministrativo : {self.getCampo()} {self.getArea()} "
        else:
            return f"\n\rAdministrativo : {self.getCampo()} {self.getArea()} "

    def getTipo(self):
        return "Administrativo"
