LOG_HISTORIAL = "historial.txt"

def ver_historial():
    try:
        with open(LOG_HISTORIAL, "r", encoding="utf-8") as archivo:
            historial = archivo.readlines()
            if historial:
                print("\nHistorial de pedidos:")
                for i, linea in enumerate(historial, start=1):
                    print(f"{i} {linea.strip()}")
            else:
                print("\nNo hay pedidos en el historial.")
    except FileNotFoundError:
        print("\nNo hay pedidos en el historial.")
