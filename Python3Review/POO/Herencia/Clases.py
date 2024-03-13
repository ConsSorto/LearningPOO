#from abc import ABC, abstractmethod
# @abstractmethod
# def mover(self):
#     pass
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


persona = Persona('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa')
print(persona)


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


alumno = Alumno('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa', 'IS', '7-9', '20222001212')
print(alumno)


class Empleado(Persona):

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__nEmp = nEmp

    def getEmp(self):
        return self.__nEmp

    def getTipo(self):
        return "Empleado"



class Visitante(Persona):
    def __init__(self, n1, n2, a1, a2, dir, razon, edificio, id):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__razon = razon
        self.__edificio = edificio


class Maestro(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion):
        super().__init__(id, n1, n2, a1, a2, dir, nEmp)
        self.__facultad = facultad
        self.__especializacion = especializacion

    def __str__(self):
        return 'ESTOY AQUI' + super().__str__() + f'Maestro : {self.getEmp()} {self.__facultad} {self.__especializacion} '

    def getTipo(self):
        return "Maestro"



maestro = Maestro('101022', 'Cons', '', 'Sorto', 'Reyes', 'Mi casa', '3234234', 'IS', 'DESARROLLO Y BASE DE DATOS')

print(maestro)


# Constructor Vacio
# Primera solucion valores por defecto en el constructor
class Administrativo(Empleado):
    # def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo):
    #     super().__init__(id, n1, n2, a1, a2, dir, nEmp)
    #     self.__area = area
    #     self.__campo = campo

    # def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
    #     super().__init__(id, n1, n2, a1, a2, dir, nEmp)

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area = "", campo = ""):
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

    def __str__(self):
        return super().__str__() + f"Administrativo : {self.getCampo()} {self.getArea()} "

    def getTipo(self):
        return "Administrativo"


class Jefe(Maestro, Administrativo):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion, area, campo, fInicio, fFin):
        Maestro.__init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion)
        Administrativo.__init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo)

        # self.setArea(area)
        # self.setCampo(campo)
        self.__finicio = fInicio
        self.__fFin = fFin

    def getTipoSuper(self):
        return super().getTipo()

    def __str__(self):
        return Maestro.__str__(self) + Administrativo.__str__(self)

jefe = Jefe('1231234', 'Nestor', 'Adrian', 'Lopez', 'Luque', 'En la casa de el', '123424', 'Facultad IS',
            'Maestria en BI', 'Base de datos', False, '20220101', '20250101')

print(Jefe.mro())
print(f"Datos del Jefe : {jefe}")

print(jefe.getTipo())
print(jefe.getTipoSuper())
