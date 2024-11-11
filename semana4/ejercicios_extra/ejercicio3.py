contador = 1
numero_actual = 0
suma_total = 0
numero = int(input("Ingrese un numero:"))

while contador <= numero:
    numero_actual = numero_actual + 1
    suma_total = suma_total + numero_actual
    contador = contador + 1
print(f"La suma de todos los numeros desde 1 a {numero} es {suma_total}")