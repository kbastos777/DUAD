counter = 1
el_mayor = 0
entrada_de_usuario = 0
print("En busca del numero mayor...")
while counter < 4:
    entrada_de_usuario = int(input("Ingrese un numero:"))
    if el_mayor < entrada_de_usuario:
        el_mayor = entrada_de_usuario
    counter=counter + 1
print(f"El numero mayor es {el_mayor}")