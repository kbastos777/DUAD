def listar_nombres_canciones(file_path):
    try:
        with open(file_path,'r',encoding='utf-8')  as file:
            lista=[]
            contador = 0
            for linea in file.readlines():
                lista.insert(contador,linea)
                contador = contador + 1
    except IndexError as ex:
        print(f"no fue posible crear la lista con exito debido a: {ex}")
    return lista


def escribir_lista(file_path,text):
    with open(file_path,'w',encoding='utf-8') as file:
        file.write(text)


def main ():
    try:
        lista_canciones = listar_nombres_canciones('nombres_de_canciones.txt')
        lista_canciones.sort()
        string_ordenado = "".join(str(element) for element in lista_canciones)
        escribir_lista('canciones_ordenadas.txt',string_ordenado)
        print(string_ordenado)
    except Exception as error:
        print(f"No es posible realizar la operacion debido a: {error}")


main()