def imprimir_cantidad_mayusculas (frase):
    counter = 0
    for string in frase:
        if string.isupper():
            counter = counter + 1
    return counter


def imprimir_cantidad_minusculas (frase):
    counter = 0
    for string in frase:
        if string.islower():
            counter = counter + 1
    return counter


def main():
    frase = "I love tsunami sushi"
    print(f"Hay {imprimir_cantidad_mayusculas(frase)} letra(s) en mayuscula(s) y {imprimir_cantidad_minusculas(frase)} minuscula(s) en la frase ")


main()