# Lista de compras interactiva

lista_compras = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Ver lista")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        item = input("Ingrese el elemento que desea agregar: ")
        lista_compras.append(item)
        print(f"{item} fue agregado a la lista.")

    elif opcion == "2":
        item = input("Ingrese el elemento que desea eliminar: ")

        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} fue eliminado de la lista.")
        else:
            print("El elemento no se encuentra en la lista.")

    elif opcion == "3":
        print("\nLista de compras:")

        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            for item in lista_compras:
                print("-", item)

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")