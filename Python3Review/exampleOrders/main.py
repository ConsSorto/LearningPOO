from orderController import getMenuOption, addOrder, showOrder, showOrders

orders = []
follow = True

while follow:
    option = getMenuOption()

    match option:
        case 1:
            addOrder(orders)
        case 2:
            showOrder()
        case 3:
            showOrders(orders)
        case 4:
            print(" Hasta luego ")
            follow = False
        case default:
            print("XXXX ingrese una opcion valida  XXXX")
