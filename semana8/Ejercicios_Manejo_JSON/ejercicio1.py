import json


def agregar_pokemon():
    try:
        diccionario_pokemon = {}
        key = "name"
        value = {"english" : input("Ingrese el nombre del pokemon:")}
        diccionario_pokemon[key] = value
        key = "type"
        value = [input("Ingrese el tipo de pokemon:")]
        diccionario_pokemon[key] = value
        key = "base"
        value = {
            "HP":int(input("Ingrese el HP:")),
            "Attack":int(input("Ingrese el nivel de Ataque:")),
            "Defense":int(input("Ingrese el nivel de defensa:")),
            "Sp. Attack":int(input("Ingrese el poder de Ataque especial:")),
            "Sp. Defense":int(input("Ingrese el nivel de defensa especial:"))
            }
        diccionario_pokemon[key] = value
    except ValueError as error:
        print(f"No se pudo realizar la operacion en la funcion agregar_pokemon debido a:{error}")
    return diccionario_pokemon


def main():
    try:
        pokemones =[
        {
            "name": {
            "english": "Pikachu"
            },
            "type": [
            "Electric"
            ],
            "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
            }
        },
        {
            "name": {
            "english": "Charmander"
            },
            "type": [
            "Fire"
            ],
            "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "Sp. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
            }
        },
        {
            "name": {
            "english": "Squirtle"
            },
            "type": [
            "Water"
            ],
            "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "Sp. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
            }
        }
        ]
        pokemones.append(agregar_pokemon())
        json.dumps(pokemones)
        print(json.dumps(pokemones,indent=4))
    except Exception as ex:
        print(f"No se pudo realizar la operacion debido a:{ex}")


main()