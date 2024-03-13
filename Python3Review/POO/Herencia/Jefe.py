from Maestro import Maestro
from Administrativo import Administrativo


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

    # def __str__(self):
    #     return Maestro.__str__(self) + Administrativo.__str__(self, False)

    def __str__(self):
        return Maestro.__str__(self) + Administrativo.__str__(self)
