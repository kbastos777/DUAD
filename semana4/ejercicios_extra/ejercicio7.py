print("Numero o suma igual a 30")

primer_numero = int(input("Ingrese el primer numero:"))
segundo_numero = int(input("Ingrese el segundo numero:"))
tercer_numero = int(input("Ingrese el tercer numero:"))

if primer_numero == 30 or segundo_numero == 30 or tercer_numero == 30 or (primer_numero + segundo_numero + tercer_numero) == 30:
    print("Correcto")
else:
    print("Incorrecto")