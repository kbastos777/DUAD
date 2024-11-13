def crear_una_lista ():
    lista=[]
    counter = 0
    while counter < 5:
        lista.insert(counter,int(input("Ingrese un numero:"))) 
        counter = counter + 1
    return lista

def crear_lista_de_numeros_primos (lista):
    lista_numeros_primos = []
    for index , record in enumerate(lista):
        divisibles = 0
        for numero in range(1,record+1,1):
            if record % numero == 0:
                divisibles = divisibles + 1
        if divisibles == 2:
            lista_numeros_primos.insert(index,record)
            divisibles = 0
    return lista_numeros_primos

def main():
    lista_creada = crear_una_lista()
    nueva_lista =  crear_lista_de_numeros_primos(lista_creada)
    print(f"Los numero(s) primo(s) de la lista son: {nueva_lista}")

main()