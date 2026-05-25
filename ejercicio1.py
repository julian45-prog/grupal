# actividad4_calificaciones.py

def analizar_calificaciones(calificaciones):
    # Calcula el promedio, la nota más alta y la más baja usando sum, len, max y min
    promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
    maxima = max(calificaciones) if calificaciones else 0
    minima = min(calificaciones) if calificaciones else 0
    
    # Retorna los resultados dentro de una tupla
    return (promedio, maxima, minima)

# 1. Lista de ejemplo (calificaciones)
notas_ejemplo = [4.5, 3.8, 2.0, 5.0, 3.2]

# 2. Prueba de la función desempaquetando la tupla de retorno
prom, nota_alta, nota_baja = analizar_calificaciones(notas_ejemplo)

# 3. Bucle for para recorrer la lista e imprimir cada nota
print("Calificaciones recibidas:")
for nota in notas_ejemplo:
    print(f"- {nota}")

# 4. Mostrar los resultados
print(f"\nResultados (Tupla): {(prom, nota_alta, nota_baja)}")
print(f"Promedio: {prom:.2f}")
print(f"Calificación más alta: {nota_alta}")
print(f"Calificación más baja: {nota_baja}")