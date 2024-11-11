descuento = 0.20 #Variable global


#Accesar a una variable definida dentro de una función desde afuera.
def definir_salario(salario):
    salario_por_hora = salario * 8
    return salario_por_hora


#Accesar a una variable global desde una función y cambiar su valor.
def calculo_de_descuento (descuento):
	descuento = descuento * 3 #Cambiar valor de la variable global
	return descuento


def main():
    print(f"El salario total es de: {definir_salario(300000)}")
    print(f"El descuento es de {calculo_de_descuento(descuento)}")
    print(salario_por_hora)


main() 