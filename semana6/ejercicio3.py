def sumar_numeros_en_lista (lista):
    suma_total = 0
    for index , record in enumerate(lista):
        suma_total = suma_total + lista[index] 
    return suma_total


def main():
    lista = [4,6,2,29]
    print(f"La suma total de todos los numeros de la lista es: {sumar_numeros_en_lista(lista)}")


main()
