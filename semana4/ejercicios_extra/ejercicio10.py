contador = 1
suma_total = 0
print("Suma de 100 numeros")

while contador <= 100:
    numero = int(input(f"Ingrese el numero en posicion {contador}: "))
    suma_total = suma_total + numero
    contador = contador + 1
print(f"La suma de todos los números es: {suma_total}")