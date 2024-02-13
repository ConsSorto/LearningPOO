carrerasLista = []
seguir = True
while seguir:
    print("        Menu             ")
    print("1. Crear carrera")
    print("2. Leer carreras")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Agregar clases")
    print("6. Salir\n")
    opcion = input("Ingrese una opcion : ")
    #verifica si la opcion es un numero entero positivo
    print("---------------------------------------------------------------")
    while True:

     if opcion.isdigit() is True:
        opcion = int(opcion)
        if (opcion >= 1) and (opcion <=6): #verifica que el numero esta dentro del rango de 1 a 6fdgffdgdfgdfgdfgdfgdfgdfgdfg
            break
        else:
            print("La opcion no esta dentro del rango permitido, intente de nuevo ")
            opcion = input()

     else:
        opcion = input("El valor no es un numero, intente de nuevo ")

    if opcion == 1:
        print("Ingrese el nombre de la carrera ")
        nombre = input()
        carreras = {}
        carreras["carrera"] = nombre #agregar la carrera al diccionario
        carreras["clases"] = [] # crear arreglo vacio paras las clases
        carrerasLista.append(carreras) #Agregar el diccionario a la lista
        print("---------------------------------------------------------------")
    elif opcion == 2:
        print(carrerasLista)
        print("---------------------------------------------------------------")
    elif opcion == 3:
        print("Ingrese el nombre de la carrera :")
        nombreBuscar = input()
        for carrera in carrerasLista:
            if carrera["carrera"] == nombreBuscar:
                print("Carrera encontrada\n")
                nombreRemplazo = input("Ingrese el nuevo nombre : ")
                carrera["carrera"] = nombreRemplazo
            else:
                print("carrera no encontrada")
        print("---------------------------------------------------------------")
    elif opcion == 4:
        print("Ingrese el nombre de la carrera a borrar :")
        nombreBuscar = input()
        for carrera in carrerasLista:
            if carrera["carrera"] == nombreBuscar:
                carrerasLista.remove(carrera)
                print(f"Carrera de {nombreBuscar} borrada con exito")
                break
            else:
                print("carrera no encontrada")
        print("---------------------------------------------------------------")

    elif opcion == 5:
        seguimineto = True
        print("Ingrese el nombre de la carrera para acceder a las clases :")
        nombreBuscar = input()
        carreraEncontrada = True
        while carreraEncontrada:
            index = 0
            for carrera in carrerasLista:
                if carrera["carrera"] == nombreBuscar:
                    print("Carrera encontrada\n")
                    carreraEncontrada = False
                    break
                else:
                    print("carrera no encontrada")
                    index += 1
            if carreraEncontrada:
                print("La carrera que ingreso no existe, intente de nuevo")
                nombreBuscar = input()

        while seguimineto:
            print("---------------------------------------------------------------")
            print(f" Menu de la carrera de {carrerasLista[index]["carrera"]}             ")
            print("1. Crear clase")
            print("2. Leer clases")
            print("3. Actualizar clase")
            print("4. Borrar clase")
            print("5. Salir\n")
            opcion = input("Ingrese una opcion : ")
            # verifica si la opcion es un numero entero positivo
            while True:
                  if opcion.isdigit() is True:
                      opcion = int(opcion)
                      if (opcion >= 1) and (opcion <= 5):  # verifica que el numero esta dentro del rango de 1 a 5
                          break
                      else:
                          print("La opcion no esta dentro del rango permitido, intente de nuevo ")
                          opcion = input()
                  else:
                      opcion = input("El valor no es un numero o es un numero negativo o decimal, intente de nuevo ")
            if opcion ==1:
                print("Ingrese el nombre de la clase ")
                nombreClase = input()
                carrerasLista[index]["clases"] += [nombreClase]  # agregar la carrera al diccionario
                print("Carrera ingresada con exito")
            elif opcion == 2:
                print(carrerasLista[index])
            elif opcion == 3:
                print("Ingrese el nombre de la clase :")
                nombreClaseBuscar = input()
                i = 0
                confirmacion = False
                for carrera in carrerasLista[index]["clases"]:
                    if carrera == nombreClaseBuscar:
                        print("Clase encontrada\n")
                        nombreRemplazo = input("Ingrese el nuevo nombre de la clase : ")
                        carrerasLista[index]["clases"][i] = nombreRemplazo #remplazar el valor el la lista de clases
                        confirmacion = True
                        break
                    else:
                        i += 1
                if not confirmacion:
                    print("La clase que esta buscando no existe ")
            elif opcion == 4:
                print("Ingrese el nombre de la clase que desea  borrar :")
                nombreBuscar = input()
                i = 0
                confirmacion = False
                for clase in carrerasLista[index]["clases"]:
                    if clase == nombreBuscar:
                        print("Clase encontrada")
                        claseEliminada = carrerasLista[index]["clases"].pop(i) #eliminamos y retornamos el valor
                        confirmacion = True
                        print(f"Clase de {claseEliminada} borrada con exito")
                        break
                    else:
                        i += 1
                if not confirmacion:
                    print("La clase que esta buscando no existe ")
            elif opcion == 5:
                print("Hasta la proxima \n ")
                seguimineto = False

    elif opcion == 6:
        print("Hasta la proxima")
        seguir = False