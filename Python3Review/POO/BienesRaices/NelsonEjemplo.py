from datetime import datetime


class Casa:
    # Direccion
    # Descripcion
    def __init__(self, gestion, direccion, descripcionCasa):
        self.__id = len(gestion.casas) + 1
        self.__direccion = direccion
        self.__descripcionCasa = descripcionCasa
        self.cuartos = []
        self.salas = []
        self.cocinas = []
        self.patios = []
        self.estados = []

    # Setters
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setDescripcionCasa(self, descripcionCasa):
        self.__descripcionCasa = descripcionCasa

    # Getters
    def getId(self):
        return self.__id

    def getDireccion(self):
        return self.__direccion

    def getDescripcionCasa(self):
        return self.__descripcionCasa


class Cocina:
    # Electrodomésticos Incluidos
    # Medidas
    # Material Desayunador
    def __init__(self, electrodomesticos, medidas, materialDesayunador):
        self.__electrodomesticos = electrodomesticos
        self.__medidas = medidas
        self.__materialDesayunador = materialDesayunador
        self.lavatrastos = []

    # Setters
    def setElectrodomesticos(self, electrodomesticos):
        self.__electrodomesticos = electrodomesticos

    def setMedidasCocina(self, medidas):
        self.__medidas = medidas

    def setMaterialDesayunador(self, materialDesayunador):
        self.__materialDesayunador = materialDesayunador

    # Getters
    def getElectrodomesticos(self):
        return self.__electrodomesticos

    def getMedidasCocina(self):
        return self.__medidas

    def getMaterialDesayunador(self):
        return self.__materialDesayunador

    def agregarLavatrastos(self, depositos, aguaCaliente):
        nuevo_Lavatrasto = Lavatrasto(depositos, aguaCaliente)
        self.lavatrastos.append(nuevo_Lavatrasto)


class Cuarto:
    # Numero de Ventanas
    # Medidas
    def __init__(self, numeroVentanas, medidas):
        self.__numeroVentanas = numeroVentanas
        self.__medidas = medidas

    # Setters
    def setNumeroVentanas(self, numeroVentanas):
        self.__numeroVentanas = numeroVentanas

    def setMedidasCuarto(self, medidas):
        self.__medidas = medidas

        # Getters

    def getNumeroVentanas(self):
        return self.__numeroVentanas

    def getMedidasCuarto(self):
        return self.__medidas


class Sala:
    # Chimenea
    # Descripción Sala
    def __init__(self, chimenea, descripcionSala):
        self.__chimenea = chimenea
        self.__descripcionSala = descripcionSala

    # Setters
    def setChimenea(self, chimenea):
        self.__chimenea = chimenea

    def setDescripcionSala(self, descripcionSala):
        self.__descripcionSala = descripcionSala

    # Getters
    def getChimenea(self):
        return self.__chimenea

    def getDescripcionSala(self):
        return self.__descripcionSala


class Lavatrasto:
    # Depositos
    # Agua-Caliente
    def __init__(self, depositos, aguaCaliente):
        self.__depositos = depositos
        self.__aguaCaliente = aguaCaliente

    # Setters
    def setDepositos(self, depositos):
        self.__depositos = depositos

    def setAguaCaliente(self, aguaCaliente):
        self.__aguaCaliente = aguaCaliente

    # Getters
    def getDepositos(self):
        return self.__depositos

    def getAguaCaliente(self):
        return self.__aguaCaliente


class Patio:
    # Área de Socialización
    # Medidas
    # Descripción
    def __init__(self, areaSocializacion, medidas, descripcionPatio):
        self.__areaSocializacion = areaSocializacion
        self.__medidas = medidas
        self.__descripcionPatio = descripcionPatio

    # Setters
    def setAreaSocializacion(self, areaSocializacion):
        self.__areaSocializacion = areaSocializacion

    def setMedidasPatio(self, medidas):
        self.__medidas = medidas

    def setDescripcionPatio(self, descripcionPatio):
        self.__descripcionPatio = descripcionPatio

    # Getters
    def getAreaSocializacion(self):
        return self.__areaSocializacion

    def getMedidasPatio(self):
        return self.__medidas

    def getDescripcionPatio(self):
        return self.__descripcionPatio


class Estado:
    # Nombre
    # Fecha
    def __init__(self, nombre, fecha):
        self.__nombre = nombre
        self.__fecha = fecha

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setFecha(self, fecha):
        self.__fecha = fecha

    # Getters
    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha


class Gestion_Clases:

    def __init__(self):
        self.casas = []

    # Métodos de Agregar
    def agregar_Casa(self, direccion, descripcionCasa):
        nueva_casa = Casa(self, direccion, descripcionCasa)
        self.casas.append(nueva_casa)

        numero_Ventanas = int(input("Ingrese el número de ventanas del Cuarto: "))
        medidas_Cuarto = input("Ingrese las medidas del cuarto: ")
        self.agregarCuartos(nueva_casa, numero_Ventanas, medidas_Cuarto)

        chimenea = input("¿La sala tiene chimenea? (Sí/No): ")
        descripcion_Sala = input("Ingrese la descripción de la sala: ")
        self.agregarSalas(nueva_casa, chimenea, descripcion_Sala)

        electrodomesticos = input("¿Electrodomésticos Incluidos? (Sí/No): ")
        medidas_Cocina = input("Ingrese las medidas de la cocina: ")
        material_Desayunador = input("Ingrese el material del Desayunador: ")
        self.agregarCocinas(nueva_casa, electrodomesticos, medidas_Cocina, material_Desayunador)

        depositos_Lavatrasto = input("¿Cuántos depósitos tiene el Lavatrastos?: ")
        agua_Caliente_Lavatrasto = input("¿El lavatrastos tienen agua caliente? (Sí/No): ")
        nueva_casa.cocinas[0].agregarLavatrastos(depositos_Lavatrasto, agua_Caliente_Lavatrasto)

        area_Socializacion = input("¿Incluye Área de Socialización? (Sí/No): ")
        medidas_Patio = input("Ingrese medidas del patio: ")
        descripcion_Patio = input("Ingrese descripción del patio: ")
        self.agregarPatios(nueva_casa, area_Socializacion, medidas_Patio, descripcion_Patio)

        tipo_Estado = int(
            input("Estado de la Casa\n1. Disponible\n2. Reservada\n3. Alquilada\n4. Vendida\nSeleccione una opción: "))
        if tipo_Estado == 1:
            estado = "Disponible"
        elif tipo_Estado == 2:
            estado = "Reservada"
        elif tipo_Estado == 3:
            estado = "Alquilada"
        elif tipo_Estado == 4:
            estado = "Vendida"
        else:
            print("Opción no válida.")
        fecha = datetime.now()
        self.agregarEstados(nueva_casa, estado, fecha)
        print("\nCasa agregada correctamente.")

    def agregarCuartos(self, casa, numeroVentanas, medidas):
        nuevo_Cuarto = Cuarto(numeroVentanas, medidas)
        casa.cuartos.append(nuevo_Cuarto)

    def agregarSalas(self, casa, chimenea, descripcionSala):
        nueva_Sala = Sala(chimenea, descripcionSala)
        casa.salas.append(nueva_Sala)

    def agregarCocinas(self, casa, electrodomesticos, medidas, materialDesayunador):
        nueva_Cocina = Cocina(electrodomesticos, medidas, materialDesayunador)
        casa.cocinas.append(nueva_Cocina)

    def agregarPatios(self, casa, areaSocializacion, medidas, descripcionPatio):
        nuevo_Patio = Patio(areaSocializacion, medidas, descripcionPatio)
        casa.patios.append(nuevo_Patio)

    def agregarEstados(self, casa, nombre, fecha):
        nuevo_Estado = Estado(nombre, fecha)
        casa.estados.append(nuevo_Estado)

    # Métodos de Visualizar
    def visualizar_Casa(self):
        if not self.casas:
            print("\nNo hay casas registradas.")

        for casa in self.casas:
            print(f"\n\t\t--- Información de la casa N. {casa.getId()} ---")
            print(f" - Dirección: {casa.getDireccion()}")
            print(f" - Descripción Casa: {casa.getDescripcionCasa()}")

            if casa.cuartos:
                print("\nCuarto: ")
                for cuarto in casa.cuartos:
                    print(f" - Numero de Ventanas: {cuarto.getNumeroVentanas()}")
                    print(f" - Medidas Cuarto: {cuarto.getMedidasCuarto()}")

            if casa.salas:
                print("Sala: ")
                for sala in casa.salas:
                    print(f" - Chimenea: {sala.getChimenea()}")
                    print(f" - Descripción Sala: {sala.getDescripcionSala()}")

            if casa.cocinas:
                print("Cocina: ")
                for cocina in casa.cocinas:
                    print(f" - Electrodomésticos: {cocina.getElectrodomesticos()}")
                    print(f" - Medidas Cocina: {cocina.getMedidasCocina()}")
                    print(f" - Material del Desayunador: {cocina.getMaterialDesayunador()}")

                    if cocina.lavatrastos:
                        print("     Lavatrastos:")
                        for lavatrasto in cocina.lavatrastos:
                            print(f"        - Depositos: {lavatrasto.getDepositos()}")
                            print(f"        - Agua Caliente: {lavatrasto.getAguaCaliente()}")

            if casa.patios:
                print("Patio: ")
                for patio in casa.patios:
                    print(f" - Área de Socialización: {patio.getAreaSocializacion()}")
                    print(f" - Medidas Patio: {patio.getMedidasPatio()}")
                    print(f" - Descripción Patio: {patio.getDescripcionPatio()}")

            if casa.estados:
                print("Estado: ")
                for estado in casa.estados:
                    print(f" - Estado: {estado.getNombre()}")
                    print(f" - Fecha: {estado.getFecha()}")

    def modificar_Casa(self):
        id_casa = int(input("Ingrese el ID de la Casa: "))

        encontrada = None
        for casa in self.casas:
            if casa.getId() == id_casa:
                encontrada = casa
                break

        if encontrada:
            nueva_Direccion = input("Ingrese la nueva direccion de la casa: ")
            nueva_Descripcion = input("Ingrese la nueva descripción de la casa: ")
            casa.setDireccion(nueva_Direccion)
            casa.setDescripcionCasa(nueva_Descripcion)
            print("\nCasa actualizada correctamente.")
        else:
            print("\nNo se encontro ninguna casa con el ID proporcionado.")

    def eliminar_Casa(self):
        id_casa = int(input("Ingrese el ID de la Casa: "))

        encontrada = None
        for casa in self.casas:
            if casa.getId() == id_casa:
                encontrada = casa
                break

        if encontrada:
            self.casas.remove(encontrada)
            print("\nCasa eliminada correctamente.")
        else:
            print("\nNo se encontro ninguna casa con el ID proporcionado.")

    def cambiar_Estado(self):
        id_casa = int(input("Ingrese el ID de la Casa: "))

        encontrada = None
        for casa in self.casas:
            if casa.getId() == id_casa:
                encontrada = casa
                break

        if encontrada:
            nuevo_estado = input("Ingrese el nuevo estado de la casa: ")
            estados_Casa = encontrada.estados

            if estados_Casa:
                estados_Casa[0].setNombre(nuevo_estado)
                estados_Casa[0].setFecha(datetime.now())
                print("\nEstado de la Casa modificado correctamente.")
            else:
                print("\nLa casa no tiene estado.")
        else:
            print("\nNo se encontro ninguna casa con el ID proporcionado.")


gestion = Gestion_Clases()

seguir = True

while (seguir):
    try:
        print("\n\t ------------ Menú -------------")
        print("1. Agregar Casa")
        print("2. Mostrar Casa")
        print("3. Actualizar Casa")
        print("4. Eliminar Casa")
        print("5. Cambiar Estado de Casa")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción no válida.")
    else:
        match opcion:
            case 1:
                direccion = input("Ingrese la dirección de la casa: ")
                descripcionCasa = input("Ingrese la descripción de la casa: ")
                gestion.agregar_Casa(direccion, descripcionCasa)
            case 2:
                gestion.visualizar_Casa()
            case 3:
                gestion.modificar_Casa()
            case 4:
                gestion.eliminar_Casa()
            case 5:
                gestion.cambiar_Estado()
            case 6:
                print("Saliendo...")
                seguir = False
            case default:
                print("Opción no válida")