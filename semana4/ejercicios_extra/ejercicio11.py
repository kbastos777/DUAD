numero_mayor = 0
contador = 1


while contador <= 100:
    numero = int(input(f"Ingrese el numero en posicion {contador}:"))
if numero > numero_mayor:
    numero_mayor = numero
contador = contador + 1
print(f"El numero mayor es {numero_mayor}")    