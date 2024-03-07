class Persona:
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
        return f'{self.getId()} {self.getN1()} {self.getN2()} {self.getA1()} {self.getA2()} '


# persona = Persona('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa')
# print(persona)
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
        return super().__str__() + f'{self.__carrera} {self.getHorario()} {self.getNcuenta()} '


# alumno = Alumno('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa', 'IS', '7-9', '20222001212')
# print(alumno)

class Empleado(Persona):

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__nEmp = nEmp

    def getEmpleado(self):
        return self.__nEmp


class Visitante(Persona):
    def __init__(self, n1, n2, a1, a2, dir, razon, edificio, id):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__razon = razon
        self.__edificio = edificio


class Maestro(Empleado):
    def __init__(self, n1, n2, a1, a2, dir, nEmp, facultad, especializacion, nEmpleado, id):
        super().__init__(id, n1, n2, a1, a2, dir, nEmpleado)
        self.__facultad = facultad
        self.__especializacion = especializacion


class Administrativo(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo):
        super().__init__(id, n1, n2, a1, a2, dir, nEmp)
        self.__area = area
        self.__campo = campo


class Jefe(Maestro, Administrativo):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion, area, campo, fInicio, fFin):
        super().__init__(n1, n2, a1, a2, dir, nEmp, facultad, especializacion, id)
        self.__finicio = fInicio
        self.__fFin = fFin

