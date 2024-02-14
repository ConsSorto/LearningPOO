import utils
from utils import getDate, getFloat, getInt
from datetime import datetime, timedelta
from params import now, menu, menuOrderTypes


def getReference(orders):
    orderNumber = -1
    while orderNumber != 0:
        orderNumber = getInt("Ingrese numero de orden (ingrese 0 para salir) : ")

        for order in orders:
            if orderNumber == int(order["numero"]):
                print("orden encontrada")
                currentDate = datetime.strptime(now, "%Y-%m-%d")
                orderDate = datetime.strptime(order["fecha"], "%Y-%m-%d")
                diffDate = orderDate - currentDate

                print(f" Dias de diferencia : {diffDate.days}")

                if diffDate.days > 0 :
                    print("No se puede aplicar garantia")
                    orderNumber = 0
                    break
                elif diffDate.days == 0 or diffDate.days > -16:
                    print("Validacion de fecha aceptada, orden garantizable")
                    return orderNumber
                else:
                    print("No se puede aplicar garantia")
                    orderNumber = 0
                    break
        else:
            print("Orden no encontrada intente de nuevo ")

    return orderNumber

def getMenuOption():
    return utils.makeMenu(menu, 1, 4)


def addOrder(orders):
    order = {}
    order["numero"] = len(orders) + 1
    order["fecha"] = getDate("Ingrese la fecha de la orden :").strftime("%Y-%m-%d")
    orderType = utils.makeMenu(menuOrderTypes, 1, 2)

    if orderType != 0:
        order["tipo"] = orderType
        if orderType == 1:
            order["precio"] = getFloat("Ingrese el precio : ")
        if orderType == 2:
            reference = getReference(orders)
            if reference != 0:
               order["referencia"] = reference
            else:
                return
    else:
        return

    orders.append(order)

def showOrder():
    pass


def showOrders(orders):
    print(orders)
