"""
Clase car para manejar los datos de automoviles, clases, instancias, metodos, utilizar variables de
clase y propias

class car:
type = "automovile"
self.doors = 4
self.id = "hbc-5254"
self.colors = ["red", "green", "blue"]
self.model = "yaris"
self.make = "toyota"
def __init__(self)
def drive(self):
def drive(self):

"""


class car:
    __type = "automovile"
    _doors = 4

    def __init__(self):
        self.make = "sin marca"
        print("inicializacion del constructor")

    def __init__(self, make):
        self.make = make
        print("inicializacion del constructor")

    def start(self):
        self.doors = 4
        self.id = "hbc-5254"
        make = "toyota"
        print("car started")

    def quantityDoors(self):
        return self.doors


class taxy:
    def __init__(self, make):
        self.car = car(make)

    def showType(self):
        print(self.car.__type)


newTaxy = taxy("acura")
newTaxy.showType()

