""" crear un dict con la siguiente tabla
    SISTEMAS    CIVIL      MATEMATICAS
    PROGRA2     SUELOS        MM110
    ALGO        DIBUJO        MM111
    POO         CARGAS        CALCULO
"""


diccionario = {"sistemas": "PROGRA2, ALGO, POO"}

print(diccionario)
diccionario2 = {}
diccionario2['clases'] = 'SISTEMAS'
print(diccionario2)

diccionario3 = {'carrera' : 'Sistemas', 'clases': ['PROGRA2', 'ALGO', 'POO'] }

diccionario4 = {'carrera' : 'Civil', 'clases': ['SUELOS', 'DIBUJO', 'CARGA'] }

diccionario5 = {'carrera' : 'Matematicas', 'clases': ['MM110', 'MM111', 'Calculo'] }

diccionario6 = {'carrera' : 'Fisca', 'clases': ['FS100', 'FS200', 'FS324', 'FS500'] }


print(diccionario3)
print(diccionario4)
print(diccionario5)
print(diccionario5)

listaCarreras = []
listaCarreras.append(diccionario3)
listaCarreras.append(diccionario4)
listaCarreras.append(diccionario5)

listaCarreras.append(diccionario6)

print(listaCarreras[2])

contador = 0
while (contador < len(listaCarreras)):
    print("-------------------------------------------")
    print("Indice " + str(contador) + " " + str(listaCarreras[contador]['carrera']))

    contador2 =0
    while(contador2 < len(listaCarreras[contador]['clases'])):
        print("    " + listaCarreras[contador]['clases'][contador2])
        contador2 +=1

    contador = contador + 1


for carrera in listaCarreras:
    print('+++++++++++++++++++++++++++++++++')
    print(carrera['carrera'])
    for clase in carrera['clases']:
        print("    " + clase)

