# Mini sistema de gestión de inventario

inventario = []

# Función para agregar productos
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")

# Función para realizar una venta
def realizar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                print("Venta realizada correctamente.")
            else:
                print("No hay suficiente cantidad disponible.")

            return

    print("Producto no encontrado.")

# Función para mostrar inventario
def mostrar_inventario():

    if len(inventario) == 0:
        print("El inventario está vacío.")

    else:
        print("\n--- INVENTARIO ---")

        for producto in inventario:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print("----------------------")

# Menú principal
while True:

    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        realizar_venta()

    elif opcion == "3":
        mostrar_inventario()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")

        