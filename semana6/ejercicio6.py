def devolver_lista(palabras):
    nueva_frase = ""
    for record in palabras:
        if record != "-":
            nueva_frase = nueva_frase + record
        else:
            nueva_frase = nueva_frase + " "
    return nueva_frase.split()


def main ():
    string_de_palabras = "perro-gato-elefante-tigre"
    lista = devolver_lista(string_de_palabras)
    lista.sort()
    nuevo_string = "-".join(str(element) for element in lista)
    print(f"El string ordenado alfabeticamente corresponde a: {nuevo_string}")


main()