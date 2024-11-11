mayor = 0
menor = 0
primero = int(input("Ingrese el primer numero:"))
segundo = int(input("Ingrese el segundo numero:"))

if primero < segundo:
    menor = primero
    mayor = segundo
    print(f"El orden de menor a mayor es: {menor} , {mayor}")
else:
    menor = segundo
    mayor = primero
    print(f"El orden de menor a mayor es: {menor} , {mayor}")