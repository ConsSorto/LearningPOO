from datetime import datetime


def makeMenu(menu, start, end):
    for item in menu:
        print(item)
    try:
        option = int(input("Ingrese la opción: "))
    except:
        return 0
    else:
        if option >= start and option <= end:
            return option
        else:
            return 0


def getDate(label):
    while (True):
        try:
            date = datetime.strptime(input(label), "%Y-%m-%d")
            return date
        except:
            print("Ingrese el formato de fecha correcto YYYY-MM-DD")

def getFloat(label):
    while (True):
        try:
            value = float(input(label))
            return value
        except:
            print("Ingrese un valor correcto, XXXX.XX")

def getInt(label):
    while (True):
        try:
            value = int(input(label))
            return value
        except:
            print("Ingrese un valor correcto, X")

