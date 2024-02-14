from datetime import datetime, timedelta

now = datetime.now().strftime("%Y-%m-%d")
print(f"  Fecha actual : {now}")

menu = ["+++++++ Menu +++++++",
        "1. Ingresar una orden",
        "2. Mostrar orden",
        "3. Mostrar todas las ordenes",
        "4. Salir"]

menuOrderTypes = ["Ingrese tipo de Orden :",
                  "1. Normal",
                  "2. Garantia",
                  "3. Ingrese cualquier numero o letra para SALIR"]
