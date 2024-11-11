import csv


def crear_diccionario():
    try:
        diccionario = {}
        key = 'nombre'
        value = input("\n\nIngrese el nombre del videojuego:")
        diccionario[key] = value
        key = 'Género'
        value = input("Ingrese el género:")
        diccionario[key] = value
        key = 'Desarrollador'
        value = input("Ingrese el desarrollador:")
        diccionario[key] = value
        key = 'Clasificación ESRB'
        value = input("Ingrese una Clasificación ESRB:")
        diccionario[key] = value
    except ValueError as error:
        print(f"Fallo en la función 'crear_diccionario', la operación no pudo ser completada debido a {error}")
    return diccionario


def crear_lista_video_juegos():
    try:
        lista_video_juegos = []
        counter = 1
        cantidad_videojuegos = int(input("Ingrese la cantidad de videojuegos:"))
        while counter <= cantidad_videojuegos:
            lista_video_juegos.insert(counter,crear_diccionario())
            counter = counter + 1
    except ValueError as ex:
        print(f"Fallo en la función 'crear_lista_video_juegos', la operación no pudo ser completada debido a:{ex}")
    return lista_video_juegos


def write_game_csv_file(file_path,data,headers):
    try:
        with open (file_path,'w',encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
    except ValueError as error:
        (f"Fallo en la función 'write_game_csv_file' la operación no pudo ser completada debido a:{error}")


def main():
    try:
        video_game_list = crear_lista_video_juegos()
        write_game_csv_file('juegos.csv',video_game_list,video_game_list[0].keys())
    except Exception as ex:
        print(f"La operacion no pudo ser completada debido a:{ex}")

main()