def retornar_frase_ordenada (frase_de_input):
    for string in range(9, -1,-1):
        print(frase_de_input[string])


def main():
    frase = "odnum aloH"
    retornar_frase_ordenada(frase)


main()