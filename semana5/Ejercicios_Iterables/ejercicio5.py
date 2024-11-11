lista=[]
counter = 0
mayor = 0

while counter <= 9:
                lista.insert(counter,int(input("Ingrese un numero:")))
                counter = counter + 1
for index in lista:
        if index > mayor:
                mayor = index
        
print(f"Numeros ingresados: {lista}")
print(f"El número mayor es {mayor}")