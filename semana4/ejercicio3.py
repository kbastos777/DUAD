import random
print("Adivine el numero secreto")
numero_usuario=0
numero_secreto=int(random.randint(1,10))
while numero_secreto != numero_usuario:
    numero_usuario = int(input("Ingrese un numero:"))
    if(numero_secreto == numero_usuario):
            print("Numero secreto descubierto!")