from menu import mostrar_menu
from pedido import pedir_cafe
from logHistorial import ver_historial

print("qué pasó?")


def main():
    while True:
        # mostrar el menú principal
        mostrar_menu()

        # pedir opción al usuario
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # pedir un café (lógica ampliada más adelante)
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\nMuchas gracias por haber tomado nuestros Oishii cafés.")
            break
        else:
            print("Opción inválida. Por favor, indique una de las opciones sugeridas.")


if __name__ == "__main__":
    main()
