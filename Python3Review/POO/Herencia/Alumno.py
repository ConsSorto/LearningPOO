from Persona import Persona


class Alumno(Persona):
    def __init__(self, id, n1, n2, a1, a2, dir, carrera, horario, ncuenta):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__carrera = carrera
        self.__horario = horario
        self.__ncuenta = ncuenta

    def getCarrera(self):
        return self.__carrera

    def getHorario(self):
        return self.__horario

    def getNcuenta(self):
        return self.__ncuenta

    def __str__(self):
        return super().__str__() + f'\n\rCarrera : {self.__carrera} {self.getHorario()} {self.getNcuenta()} '

# alumno = Alumno('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa', 'IS', '7-9', '20222001212')
# print(alumno)
