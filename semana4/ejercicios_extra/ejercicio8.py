mayor = 0
contador = 1


while contador <= 5:
    numero = int(input("Ingrese un numero:"))
    if numero > mayor:
        mayor = numero
    contador = contador + 1
print(f"El numero mayor es {mayor}")  