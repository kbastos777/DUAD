def Suma (numero_actual):
    nuevo_numero_actual = 0
    try:
        numero_usuario=int(input("\nIngrese un numero a sumar:")) 
        nuevo_numero_actual =  numero_actual + numero_usuario
    except ValueError as error:
        print(f"\nHa Ocurrido un error en la funcion Suma, debido a que el dato ingresado por el usuario es invalido:{error}")
    print(f"\nEl resultado de la suma entre {numero_actual} y {numero_usuario} es: {nuevo_numero_actual}")    
    return nuevo_numero_actual


def Resta (numero_actual):
    nuevo_numero_actual = 0
    try:
        numero_usuario=int(input("\nIngrese un numero a restar:"))
        nuevo_numero_actual =  numero_actual - numero_usuario
    except ValueError as error:
        print(f"\nHa Ocurrido un error en la funcion Resta, debido a que el dato ingresado por el usuario es invalido:{error}")
    print(f"\nEl resultado de la resta entre {numero_actual} y {numero_usuario} es: {nuevo_numero_actual}")  
    return nuevo_numero_actual


def Multiplicacion (numero_actual):
    nuevo_numero_actual = 0
    try:
        numero_usuario=int(input("\nIngrese un numero a multiplicar:"))
        nuevo_numero_actual =  numero_actual * numero_usuario
    except ValueError as error:
        print(f"\nHa Ocurrido un error en la funcion Multiplicacion, debido a que el dato ingresado por el usuario es invalido:{error}")
    print(f"\nEl resultado de la multiplicacion entre {numero_actual} y {numero_usuario} es: {nuevo_numero_actual}")  
    return nuevo_numero_actual


def Division (numero_actual):
    nuevo_numero_actual = 0
    try:
        numero_usuario=int(input("\nIngrese un numero a dividir:"))
        nuevo_numero_actual =  numero_actual / numero_usuario
    except ValueError as error:
        print(f"\nHa Ocurrido un error en la funcion Division, debido a que el dato ingresado por el usuario es invalido:{error}")
    print(f"\nEl resultado de la divicion entre {numero_actual} y {numero_usuario} es: {nuevo_numero_actual}")  
    return nuevo_numero_actual


def Borrar_resultado (numero_actual):
    numero_actual = 3
    return numero_actual


def main():
    numero_actual = 3
    while True:
        try:
            
            print("\n\n\nMenu de Calculadora")
            print("\nOpcion 1: Sumar")
            print("Opcion 2: Restar")
            print("Opcion 3: Multiplicar")
            print("Opcion 4: Dividir")
            print("Opcion 5: Borrar resultado")
            print("Opcion 6: Salir")
            opcion = int(input("\nIngrese una opcion:"))
            if opcion == 1:
                numero_actual = Suma(numero_actual)
            elif opcion ==2:
                numero_actual = Resta(numero_actual)
            elif opcion ==3: 
                numero_actual = Multiplicacion(numero_actual)
            elif opcion == 4:
                numero_actual = Division(numero_actual)
            elif opcion == 5:
                numero_actual = Borrar_resultado(numero_actual)
            elif opcion == 6:
                print("\nSaliendo del programa...")
                break
            else:
                raise Exception()
        except Exception as ex:
            print(f"\nLa operacion no pudo ser realizada debido a: {ex}")

main()
