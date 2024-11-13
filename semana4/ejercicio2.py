nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

if(edad <= 3):
        print(f"{nombre} {apellido} es un bebe")
elif(edad < 13 and edad >= 4):
        print(f"{nombre} {apellido} es un niño")
elif(edad < 16 and edad >= 13 ):
        print(f"{nombre} {apellido} es un preadolescente")
elif(edad < 18 and edad >= 16 ):
        print(f"{nombre} {apellido} es un adolescente")
elif(edad < 25 and edad >= 18 ):
        print(f"{nombre} {apellido} es un adulto joven")
elif(edad < 60 and edad >= 25 ):
        print(f"{nombre} {apellido} es un adulto")
else:
        print(f"{nombre} {apellido} es un adulto mayor")
        