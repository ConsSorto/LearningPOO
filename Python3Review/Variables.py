print("hola mundo")
varEntero = 1
varFloat = 1.1
varString = "Tipo String"
varBoolean = True


print(varBoolean)
print(varEntero)
print(varString)

varLista = [1,3,4,5]

print(varLista)

varTupla = (1,2,3,4)

print(varTupla)

varDiccionario = {"nombre" : "Cons", "apellido" : "sorto"}

print(varDiccionario)

varDiccionario["subdiccionario"] = {"direccion": "San Francisco"}

print(varDiccionario)

print(type(varDiccionario))
print(type(varEntero))

varEntero2 = 0.2

if varEntero2 > varEntero:
    print(str(varEntero2) + " es mayor que " + str(varEntero))
else:
    if varEntero2 == varEntero:
        print("son iguales")
    else:
        print(str(varEntero2) + " es menor que " + str(varEntero))

if varEntero2 > varEntero:
    print(str(varEntero2) + " es mayor que " + str(varEntero))
elif varEntero2 == varEntero:
    print("son iguales")
else:
    print(str(varEntero2) + " es menor que " + str(varEntero))

verEntero = True



varMarch = 4

match(varMarch):
    case 1:
        print("opcion 1")
    case 2:
        print("opcion 2")
    case default:
        print("opcion por defecto")


