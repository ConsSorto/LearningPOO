"""
    crear un dict con la siguiente tabla
    SISTEMAS    CIVIL      MATEMATICAS
    PROGRA2     SUELOS        MM110
    ALGO        DIBUJO        MM111
    POO         CARGAS        CALCULO

    Crear
    Leer
    Actualizar
    Borrar

    Crear las carreras
    Crear las clases
"""









carreras = []
seguir = True

while seguir:
    print(carreras)
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))

    print("----------------------------------")
    if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre : ")
        dicCarrera = {}
        dicCarrera["carrera"] = nombre
        carreras.append(dicCarrera)
    elif opcion == 2:
        print("Leer (mostrar) carreras")
        for carrera in carreras:
            print("- Nombre :" + carrera["carrera"])
    elif opcion == 3:
        carreraActualizar = input("Ingrese nombre de la carrera : ")
        nuevoValor = input("Ingrese nuevo nombre de la carrera : ")

        indice = 0
        for carrera in carreras:
            if carrera["carrera"] == carreraActualizar:
                carrera["carrera"] = nuevoValor

        """
        indice = 0
        for carrera in carreras:
            if carrera["carrera"] == carreraActualizar:
                break
            else:
                indice = indice + 1

        carreras[indice]["carrera"] = nuevoValor
        """
    elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera : ")
        indice = 0
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == carreraBorrar:
                encontrado = True
                break
            else :
                indice = indice + 1

        if encontrado :
            carreras.remove(carreras[indice])
            print("Elemento borrado")
        else:
            print("No existe")
    elif opcion == 5:
        print("Hasta la proxima")
        seguir = False
    print("----------------------------------")

"""
[0  {'carrera': 'IS'},
 1  {'carrera': 'CIVIL'},
 2  {'carrera': 'IND'}]

"""
