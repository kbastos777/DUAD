print("Calcular si un numero es divisible entre 3 , 5 o ambos ")
numero_usuario = int(input("Ingrese un numero:"))

if (numero_usuario % 3) == 0 and (numero_usuario % 5) == 0:
    print("FizzBuzz")
elif (numero_usuario % 3) == 0:
    print("Fizz")
elif (numero_usuario % 5) == 0:
    print("Buzz")
else:
    print(f"El numero {numero_usuario} no es divisible entre 3 y 5")