casas = []


class Cuarto:

    def __init__(self, ventanas, medida):
        self.__ventanas = ventanas
        self.__medida = medida

    def getVentanas(self):
        return self.__ventanas

    def setventanas(self, valor):
        self.__ventanas = valor

    def getmedidas(self):
        return self.__medida


    def setmedidas(self, valor):
        self.__medidas = valor

    def __str__(self):
        return f"El cuarto cuenta con {self.getventanas} ventanas, mide {self.getmedidas}"


class Sala:
    def __init__(self, chimenea, descripcion, ):
        self.__chimena = chimenea
        self.__descripcion = descripcion

    def getchimenea(self):
        return self.__chimena

    def setchimenea(self, valor):
        self.__chimenea = valor

    def getdescripcion(self):
        return self.__descripcion

    def setdescripcion(self, valor):
        self.__descripcion = valor

    def __str__(self):
        return f"descripcion de la sala: {self.getdescripcion},{"cuenta con chimenea" if self.getchimenea else "no cuenta con chimenea"}"


class Lavatrastes:
    def __init__(self, depositos, agua):
        self.__depositos = depositos
        self.__agua = agua

    def getdepositos(self):
        return self.__depositos

    def setdepositos(self, valor):
        self.__depositos = valor

    def getagua(self):
        return self.__agua

    def setagua(self, valor):
        self.__agua = valor

    def __str__(self):
        return f"Lavatrastes con {self.getdepositos} huecos y {"agua caliente" if self.getagua else "agua helada"}."


class Cocina:

    def __init__(self, descripcion, electrodomesticos, medidas, material, lavatrastes):
        self.__descripcion = descripcion
        self.__electrodomesticos = electrodomesticos
        self.__medidas = medidas
        self.__material = material
        self.lavatrastes = lavatrastes

    def getdescripcion(self):
        return self.__descripcion

    def setdescripcion(self, valor):
        self.__descripcion = valor

    def getelectrodomesticos(self):
        return self.__electrodomesticos

    def setelectrodomesticos(self, valor):
        self.__electrodomesticos = valor

    def getmedidas(self):
        return self.__medidas

    def setmedidas(self, valor):
        self.__medidas = valor

    def getmaterial(self):
        return self.__material

    def setmaterial(self, valor):
        self.__material = valor

    def __str__(self):
        electricos = "con electrodomesticos" if self.getelectrodomesticos() else "sin electrodomesticos"
        return f"La cocina cuenta con {self.getmedidas()}, {electricos}, el material del comedor es {self.getmaterial} descripción: {self.getdescripcion()}"


class Patio:
    def __init__(self, medidas, areaSocial, descripcion):
        self.__medidas = medidas
        self.__areaSocial = areaSocial
        self.__descripcion = descripcion

    def getmedidas(self):
        return self.__medidas

    def setmedidas(self, valor):
        self.__medidas = valor

    def getareaSocial(self):
        return self.__areaSocial

    def setareaSocial(self, valor):
        self.__areaSocial = valor

    def getdescripcion(self):
        return self.__descripcion

    def setdescripcion(self, valor):
        self.__descripcion = valor

    def __str__(self):
        areasocial = "con área social" if self.getareaSocial() else "sin área social"
        return f"El patio cuenta con medidas de {self.getmedidas()}, {areasocial}, descripción: {self.getdescripcion()}"


class Estado:
    def __init__(self, estado, fecha):
        self.__estado = estado
        self.__fecha = fecha

    def getestado(self):
        return self.__estado

    def setestado(self, valor):
        self.__estado = valor

    def getfecha(self):
        return self.__fecha

    def setfecha(self, valor):
        self.__fecha = valor

    def __str__(self):
        return f"El estado de la casa es{self.getestado} con fecha {self.getfecha}"





class Casa:
    def __init__(self, direccion, ):
        self.__direccion = direccion
        self.__cuartos = []
        self.__salas = []
        self.__cocinas = []
        self.__patios = []
        self.__estados = []

    def agregarcuarto(self, cuarto):
        self.__cuartos.append(cuarto)

    def agregarsala(self, sala):
        self.__salas.append(sala)

    def agregarcocina(self, cocina):
        self.__cocinas.append(cocina)

    def agregarpatio(self, patio):
        self.__patios.append(patio)

    def agregarestado(self, estado):
        self.__estados.append(estado)

    def getcuartos(self):
        cuartos = {}
        for i, cuarto in enumerate(self.__cuartos, start=1):
            for j, cuart in enumerate(cuarto, start=1):
                cuartos[f"cuarto# {i}"] = cuart
        return cuartos

    def getcocinas(self):
        cocinas = {}
        for i, cocina in enumerate(self.__cocinas, start=1):
            cocinas[f"cocina# {i}"] = cocina
        return cocinas



    def obtenerDatos(self, contenedor):
        datos = {}
        for i, item in enumerate(contenedor, start=1):
            datos[f"# {i} "] = item
        return datos

    def getpatios(self):
        return self.obtenerDatos(self.__patios)

    def getestados(self):
        return self.obtenerDatos(self.__estados)
    def getsalas(self):
        salas = {}
        for i, sala in enumerate(self.__salas, start=1):
            salas[f"sala# {i}"] = sala
        return salas

    def __str__(self):
        # return f"Casa con direccion {self.__direccion},cuenta con {self.__salas} {self.__cuartos}\n tambien tiene {self.__cocinas}\n,incluye tambien {self.__patios}\n, la casa ha estado en estos estados {self.getestados}"
        return f"Casa con direccion {self.__direccion},cuenta con {self.getsalas()}\n tambien tiene {self.getcuartos}\n,incluye tambien {self.getcocinas()}\n, la casa ha estado en estos estados {self.getpatios()},{self.getestados()}"


def menu():
    casas = []
    while True:
        print("\n1. Agregar Casa")
        print("2. Mostrar Casas")
        print("3. Modificar Casa")
        print("4. Eliminar Casa")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            direccion = input("Ingrese la dirección de la casa: ")
            casa = Casa(direccion)
            while True:
                print("\nAgregar:")
                print("1. Cuarto")
                print("2. Sala")
                print("3. Cocina")
                print("4. Patio")
                print("5. Estado")
                print("6. Terminar de agregar")
                opcion_agregar = input("Seleccione una opción para agregar a la casa: ")
                salas = []
                cuartos = []
                cocinas = []
                patios = []
                estados = []
                if opcion_agregar == "1":
                    ventanas = input("Ingrese el número de ventanas del cuarto: ")
                    medida = input("Ingrese la medida del cuarto: ")
                    cuarto = Cuarto(ventanas, medida)
                    cuartos.append(cuarto)

                    print("Cuarto agregado correctamente.")
                elif opcion_agregar == "2":
                    chimenea = input("¿La sala cuenta con chimenea?1. si, 2. no ")
                    booleano = False
                    if chimenea == 1:
                        booleano = True
                    elif chimenea == 2:
                        booleano = False
                    descripcion = input("Ingrese una descripción de la sala: ")
                    sala = Sala(booleano, descripcion)
                    salas.append(sala)

                    print("Sala agregada correctamente.")
                elif opcion_agregar == "3":
                    descripcion = input("Ingrese una descripción de la cocina: ")
                    electrodomesticos = input("¿La cocina cuenta con electrodomésticos? 1. si, 2. no ")
                    booleano1 = False
                    booleano2 = False
                    if electrodomesticos == 1:
                        booleano1 = True
                    elif electrodomesticos == 2:
                        booleano1 = False
                    medidas = input("Ingrese las medidas de la cocina: ")
                    material = input("Ingrese el material del comedor: ")
                    lavatrastes_depositos = input("Ingrese el número de depósitos del lavatrastes: ")
                    lavatrastes_agua = int(input("¿El lavatrastes cuenta con agua caliente? 1. si, 2. no "))
                    if lavatrastes_agua == 1:
                        booleano2 = True
                    elif lavatrastes_agua == 2:
                        booleano2 = False
                    lavatrastes = Lavatrastes(lavatrastes_depositos, booleano2)
                    cocina = Cocina(descripcion, booleano1, medidas, material, lavatrastes)
                    cocinas.append(cocina)

                    print("Cocina agregada correctamente.")
                elif opcion_agregar == "4":
                    medidas = input("Ingrese las medidas del patio: ")
                    areaSocial = int(input("¿El patio cuenta con área social? 1. si, 2. no "))
                    booleano = False
                    if areaSocial == 1:
                        booleano = True
                    elif areaSocial == 2:
                        booleano = False
                    descripcion = input("Ingrese una descripción del patio: ")
                    patio = Patio(medidas, booleano, descripcion)
                    patios.append(patio)

                    print("Patio agregado correctamente.")
                elif opcion_agregar == "5":
                    estado = input("Ingrese el estado de la casa: ")
                    fecha = input("Ingrese la fecha del estado: ")
                    estadoobjeto = Estado(estado, fecha)
                    estados.append(estadoobjeto)

                    print("Estado agregado correctamente.")
                elif opcion_agregar == "6":
                    casa.agregarcuarto(cuartos)
                    casa.agregarsala(salas)
                    casa.agregarcocina(cocinas)
                    casa.agregarpatio(patios)
                    casa.agregarestado(estados)
                    casas.append(casa)
                    print("Casa agregada correctamente.")

                    break

                else:
                    print("Opción no válida. Intente de nuevo.")


        elif opcion == "2":
            for i, casa in enumerate(casas, start=1):
                print(f"casa# {i},{casa}")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")


menu()