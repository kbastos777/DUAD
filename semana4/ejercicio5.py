print("Calculadora de puntajes")
counter = 1
cantidad_notas_reprobadas = 0
promedio_reprobadas = 0
cantidad_notas_aprobadas = 0
promedio_aprobadas = 0
suma_aprobadas = 0
suma_reprobadas = 0
cantidad_de_notas = int(input("Ingrese la cantidad de notas:"))

while counter <= cantidad_de_notas:
    nota = int(input("Ingrese la nota:"))
    if(nota < 70):
        cantidad_notas_reprobadas = cantidad_notas_reprobadas + 1
        suma_reprobadas = suma_reprobadas + nota
        promedio_reprobadas = suma_reprobadas / cantidad_notas_reprobadas
    else:
        cantidad_notas_aprobadas = cantidad_notas_aprobadas + 1
        suma_aprobadas = suma_aprobadas + nota
        promedio_aprobadas = suma_aprobadas / cantidad_notas_aprobadas
    counter = counter + 1
print(f"Cantidad de notas aprobadas: {cantidad_notas_aprobadas}")
print(f"Cantidad de notas reprobadas a 70: {cantidad_notas_reprobadas}")
print(f"El promedio de todas las notas es: {(suma_aprobadas + suma_reprobadas) / cantidad_de_notas }")
print(f"El promedio de notas aprobadas es: {promedio_aprobadas }")
print(f"El promedio de notas reprobadas es: {promedio_reprobadas}")