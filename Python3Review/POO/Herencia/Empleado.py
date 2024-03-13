from Persona import Persona


class Empleado(Persona):

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
        Persona.__init__(self, id, n1, n2, a1, a2, dir)
        self.__nEmp = nEmp

    def getEmp(self):
        return self.__nEmp

    def getTipo(self):
        return "Empleado"

    # def __str__(self, mostrarEmpleado):
    #     if mostrarEmpleado:
    #         return Persona.__str__(self) + f'\n\rEmpleado : {self.__nEmp}'
    #     else:
    #         return f''

    def __str__(self):
        return Persona.__str__(self) + f'\n\rEmpleado : {self.__nEmp}'
