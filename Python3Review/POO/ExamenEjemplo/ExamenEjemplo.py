from abc import ABC, abstractmethod


class Producto(ABC):
    """
    codigo, marca, modelo, costo, existencia
    """

    def __init__(self, codigo, marca, modelo, costo, existencia):
        self.__codigo = codigo
        self.__marca = marca
        self.__modelo = modelo
        self.__costo = costo
        self.__existencia = existencia

    def impuesto(self):
        return self.impuestoProducto(self)

    def strProductoBase(self):
        return f"Codigo: {self.__codigo} Marca: {self.__marca} Modelo: {self.__modelo} Costo: {self.__costo} Existencia: {self.__existencia} Precio Venta: {self.precioVenta()} Impuesto : {self.impuesto()} "


    @abstractmethod
    def precioVenta(self):
        pass

    @abstractmethod
    def strProducto(self):
        pass

    @staticmethod
    def impuestoProducto(producto):
        return producto.precioVenta() * 0.15

    @staticmethod
    def aplicarDescuento(productos, codigo, porcentaje):
        if porcentaje > 100:
            print("no se puede aplicar el descuento")

        precioReal = -1

        for producto in productos:
            if producto._codigo == codigo:
                precioReal = producto.precioVenta()
                precioDescuento = precioReal - (precioReal * (porcentaje / 100))
                print(f"Precio Real :{precioReal}, Precio Descuento :{precioDescuento}")
                break

        if precioReal == -1:
            print("Producto no encontrado")

        return producto.precioVenta() * 0.15

    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, value):
        self.__modelo = value

    @property
    def _costo(self):
        return self.__costo

    @_costo.setter
    def _costo(self, value):
        self.__costo = value

    @property
    def _existencia(self):
        return self.__existencia

    @_existencia.setter
    def _existencia(self, value):
        self.__existencia = value


# ---------------------------------------------------------------------------------------------------------------------
class Refrigeradora(Producto):
    """
    puertas, tamano, tieneFreezer, divisiones, dispensadorAgua
    """

    def __init__(self, codigo, marca, modelo, costo, existencia, puertas, tamano, tieneFreezer, divisiones,
                 dispensadorAgua):
        # Producto.__init__(self, codigo, marca, modelo, costo, existencia)
        super().__init__(codigo, marca, modelo, costo, existencia)
        self.puertas = puertas
        self.tamano = tamano
        self.tieneFreezer = tieneFreezer
        self.dispensadorAgua = dispensadorAgua
        self.divisiones = divisiones

    def precioVenta(self):
        if self.puertas == 2:
            return self._costo * 1.70
        else:
            return self._costo * 1.65

    def strProducto(self):
        label = f"Puerta: {self.puertas} Tamano : {self.tamano} Tiene Freezer {self.tieneFreezer} dispensadorAgua : {self.dispensadorAgua} Divisiones : {self.divisiones}"
        return self.strProductoBase() + label

# ---------------------------------------------------------------------------------------------------------------------
class Televisor(Producto):
    """
    tecnologia, tamano, fullHD, tamanoMarco, empotrable
    """

    def __init__(self, codigo, marca, modelo, costo, existencia, tecnologia, tamano, fullHD, tamanoMarco, empotrable):
        # Producto.__init__(self, codigo, marca, modelo, costo, existencia)
        super().__init__(codigo, marca, modelo, costo, existencia)
        self.tecnologia = tecnologia
        self.tamano = tamano
        self.fullHD = fullHD
        self.tamanoMarco = tamanoMarco
        self.empotrable = empotrable

    def precioVenta(self):
        if self.tamano >= 75:
            return self._costo * 2
        elif self.tamano >= 60 and self.tamano < 75:
            return self._costo * 1.80
        elif self.tamano < 60:
            return self._costo * 1.75

    def strProducto(self):
        label = f"Tecnologia: {self.tecnologia} Tamano: {self.tamano} fullHD: {self.fullHD} tamanoMarco: {self.tamanoMarco} empotrable: {self.empotrable}"
        return self.strProductoBase() + label

# ---------------------------------------------------------------------------------------------------------------------
class Celular(Producto):
    """
    tecnologia, verAndroid, camaraFrontal, camaraPrincipal, serviciosGoogle
    """

    def __init__(self, codigo, marca, modelo, costo, existencia, tecnologia, verAndroid, camaraFrontal, camaraPrincipal,
                 serviciosGoogle):
        # Producto.__init__(self, codigo, marca, modelo, costo, existencia)
        super().__init__(codigo, marca, modelo, costo, existencia)
        self.tecnologia = tecnologia
        self.verAndroid = verAndroid
        self.camaraFrontal = camaraFrontal
        self.camaraPrincipal = camaraPrincipal
        self.serviciosGoogle = serviciosGoogle

    def precioVenta(self):
        return self._costo * 2.5

    def strProducto(self):
        label = f"Tecnologia: {self.tecnologia} verAndroid: {self.verAndroid} camaraFrontal: {self.camaraFrontal} camaraPrincipal: {self.camaraPrincipal} serviciosGoogle: {self.serviciosGoogle}"
        return self.strProductoBase() + label

# ---------------------------------------------------------------------------------------------------------------------
def validarCodigo(codigo):
    for producto in productos:
        if producto._codigo == codigo:
            return "existe"

    return codigo

# ---------------------------------------------------------------------------------------------------------------------
def setProductoBase():
    productoBase = {}

    productoBase['codigo'] = validarCodigo(input("Ingrese codigo del producto: "))

    if productoBase['codigo'] == "existe":
        print("Producto no ingresado, codigo ya existe")
        return "error"

    productoBase['marca'] = input("Ingrese Marca :")
    productoBase['modelo'] = input("Ingrese Modelo :")

    try:
        productoBase['costo'] = float(input("Ingrese Costo :"))
        if productoBase['costo'] < 0:
            print("dato mal ingresado, costo tiene que se mayor a 0")
            return "error"
    except:
        print("dato mal ingresado, no se agrega el producto")
        return "error"
    else:
        productoBase['existencia'] = input("Ingrese Existencia :")

    return productoBase

# ---------------------------------------------------------------------------------------------------------------------
def getFloat(label):
    while (True):
        try:
            value = float(input(label))
            return value
        except:
            print("Ingrese un valor correcto, XXXX.XX")

# ---------------------------------------------------------------------------------------------------------------------
def getSINO(label):
    while (True):
        value = input(label).upper()
        if value == "SI" or value == "NO":
            return value
        else:
            print("Ingrese un valor correcto, SI o NO")
            continue

# ---------------------------------------------------------------------------------------------------------------------
def setCelular():
    celular = {}

    celular['tecnologia'] = input("Ingrese Tecnologia :")
    celular['verAndroid'] = getFloat("Ingrese VerAndroid :")
    celular['camaraFrontal'] = getFloat("Ingrese camaraFrontal :")
    celular['camaraPrincipal'] = getFloat("Ingrese camaraPrincipal :")
    celular['serviciosGoogle'] = getSINO("Ingrese serviciosGoogle (SI o NO):")

    return celular


# ---------------------------------------------------------------------------------------------------------------------
seguir = True
productos = []

menuPrincipal = ["+++++++ Menu +++++++",
                 "1. Ingresar Refrigeradora",
                 "2. Ingresar Televisor",
                 "3. Ingresar Celular",
                 "4. Mostrar Productos",
                 "5. Ingresar Descuentos",
                 "6. Salir"]

while seguir:
    print(productos)
    for item in menuPrincipal:
        print(item)
    try:
        option = int(input("Ingrese la opción: "))
    except:
        print("XXXX ingrese una opcion valida  XXXX")
    else:
        match option:
            case 1:
                codigo = validarCodigo(input("Ingrese codigo del producto: "))

                if codigo == "existe":
                    print("Producto no ingresado, codigo ya existe")
                    continue

                marca = input("Ingrese Marca :")
                modelo = input("Ingrese Modelo :")

                try:
                    costo = float(input("Ingrese Costo :"))

                    if costo < 0:
                        print("dato mal ingresado, costo tiene que se mayor a 0")
                        continue
                except:
                    print("dato mal ingresado, no se agrega el producto")
                    continue
                else:
                    existencia = input("Ingrese Existencia :")

                try:
                    puertas = int(input("Ingrese puertas :"))
                except:
                    print("dato mal ingresado, no se agrega el producto")
                    continue
                else:
                    tamano = input("Ingrese Tamano :")
                    tieneFreezer = input("Ingrese tieneFreezer :")
                    dispensadorAgua = input("Ingrese dispensadorAgua :")
                    divisiones = input("Ingrese divisiones :")

                refrigeradora = Refrigeradora(codigo, marca, modelo, costo, existencia, puertas, tamano, tieneFreezer,
                                              dispensadorAgua, divisiones)

                productos.append(refrigeradora)
            case 2:
                productoBase = setProductoBase()
                if productoBase == "error":
                    continue

                tecnologia = input("Ingrese tecnologia :")
                try:
                    tamano = int(input("Ingrese tamano :"))
                except:
                    print("dato mal ingresado, no se agrega el producto")
                    continue
                else:
                    fullHD = input("Ingrese fullHD :")
                    tamanoMarco = input("Ingrese tamanoMarco :")
                    empotrable = input("Ingrese empotrable :")

                    televisor = Televisor(productoBase['codigo'],productoBase['marca'] ,productoBase['modelo'] , productoBase['costo'], productoBase['existencia'], tecnologia, tamano, fullHD, tamanoMarco, empotrable)

                    productos.append(televisor)
            case 3:
                productoBase = setProductoBase()
                if productoBase == "error":
                    continue
                celularDatos = setCelular()

                celular = Celular(productoBase['codigo'], productoBase['marca'], productoBase['modelo'],
                                  productoBase['costo'], productoBase['existencia'], celularDatos['tecnologia'],
                                  celularDatos['verAndroid'], celularDatos['camaraFrontal'],
                                  celularDatos['camaraPrincipal'], celularDatos['serviciosGoogle'])

                productos.append(celular)
            case 4:
                for producto in productos:
                    print(producto.strProducto())
            case 5:
                codigo = input("Ingrese el codigo del producto : ")
                descuento = getFloat("Ingrese el descuento (%) : ")
                Producto.aplicarDescuento(productos, codigo, descuento)
            case 6:
                print("Hasta Luego")
                seguir = False
            case default:
                print("XXXX ingrese una opcion valida  XXXX")
