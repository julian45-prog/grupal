# Conversor de unidades

# Diccionario con factores de conversión
conversiones = {
    ("metros", "pies"): 3.28084,
    ("kilogramos", "libras"): 2.20462,
    ("litros", "galones"): 0.264172
}

# Función para convertir unidades
def convertir(cantidad, origen, destino):

    if (origen, destino) in conversiones:
        factor = conversiones[(origen, destino)]
        resultado = cantidad * factor
        return resultado

    else:
        return "Conversión no disponible."

# Programa principal
cantidad = float(input("Ingrese la cantidad: "))
unidad_origen = input("Ingrese la unidad de origen: ").lower()
unidad_destino = input("Ingrese la unidad de destino: ").lower()

resultado = convertir(cantidad, unidad_origen, unidad_destino)

print("Resultado:", resultado)