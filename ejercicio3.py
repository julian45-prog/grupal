# Agenda de contactos con diccionario

agenda = {}

# Función para añadir contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado correctamente.")

# Función para buscar contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")

    if nombre in agenda:
        print(f"El teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print("El contacto no existe.")

# Función para mostrar contactos
def mostrar_contactos():
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("\n--- CONTACTOS ---")

        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()

    elif opcion == "2":
        buscar_contacto()

    elif opcion == "3":
        mostrar_contactos()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")