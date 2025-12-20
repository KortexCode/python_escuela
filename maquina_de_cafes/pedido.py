from datetime import datetime


def pedir_cafe():
    LOG_HISTORIAL = "historial.txt"
    cafes = {"1": "expreso", "2": "capuchino", "3": "latte", "4": "americano"}
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nElige el café que prefieras:")
    opcion = elegir_opcion()
    ## Valida la opción ingresada
    while opcion not in ["1", "2", "3", "4"]:
        print("\nOpción inválida. Por favor, elege un café válido.")
        opcion = elegir_opcion()
    # Registra el pedido en el historial

    print(f"\nHas pedido un {cafes[opcion]}. ")
    print(f"\nPreparando un {cafes[opcion]}.....")
    # Crear archivo de historial si no existe y agregar el pedido
    with open(LOG_HISTORIAL, "a", encoding="utf-8") as archivo:
        archivo.write(f"{cafes[opcion]} - {fecha_actual}\n")


def elegir_opcion():
    print("1. Expreso")
    print("2. Capuchino")
    print("3. Latte")
    print("4. Americano")
    return input("Opción: ")
