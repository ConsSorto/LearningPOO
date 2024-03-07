class Patio:
    """
    areaSocial
    medidas
    descripcion
    """
    def __init__(self, areaSocial, medidas, descripcion):
        self.__areaSocial = areaSocial
        self.__medidas = medidas
        self.__descripcion = descripcion

    def getAreaSocial(self):
        return self.__areaSocial
    def getMedidas(self):
        return self.__medidas

    def getDescripcion(self):
        return self.__descripcion

    def setAreaSocial(self, areaSocial):
        self.__areaSocial = areaSocial

    def setMedidas(self, medidas):
        self.__medidas = medidas

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

class Lavatrastos:
    """
    depositos
    aguaCaliente
    """
    def __init__(self, depositos, aguaCaliente):
        self.__depositos = depositos
        self.__aguaCaliente = aguaCaliente

    def getDepositos(self):
        return self.__depositos

    def getAguaCaliente(self):
        return self.__aguaCaliente

    def setDepositos(self, depositos):
        self.__depositos = depositos

    def setAguaCaliente(self, aguaCaliente):
        self.__aguaCaliente = aguaCaliente

