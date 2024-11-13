import os
from utilities.actions import add_student_data,return_json_format,top_three_best_students,show_student_averages
from utilities.data import write_csv,rewrite_csv


def print_main_menu_options ():
    print("\n\n##### Bienvenido al Sistema Estudiantil ######## \n\n")
    print("Menu principal")
    print("Opcion 1: Ingresar informacion de n estudiantes")
    print("Opcion 2: Ver informacion de todos los estudiantes ingresados")
    print("Opcion 3: Ver el top 3 de los estudiantes con la mejor nota promedio")
    print("Opcion 4: Ver la nota promedio entre las notas de todos los estudiantes")
    print("Opcion 5: Exportar todos los datos actuales a un archivo CSV")
    print("Opcion 6: Importar los datos de un archivo CSV previamente exportado")
    print("Opcion 7: Salir\n\n")


def execute_main_menu ():
    os.system('CLS')
    student_database = []
    counter = 1
    while True:
        try:
            print_main_menu_options()
            option = int(input("Ingrese una opcion:"))
            if option == 1:
                quantity=int(input("Ingrese la cantidad de estudiantes:"))
                while counter <= quantity:
                    student_database.insert(quantity,add_student_data(counter))
                    counter = counter + 1
            elif option == 2:
                os.system('CLS')
                print("\n\n\n###Lista de informacion por estudiante###\n\n")
                print(return_json_format(student_database))
            elif option == 3:
                top_three_best_students(student_database)
            elif option == 4:
                show_student_averages(student_database)
            elif option == 5:
                write_csv('Base_de_datos_estudiantil.csv',student_database,student_database[0].keys())
            elif option == 6:
                rewrite_csv('Base_de_datos_estudiantil.csv',student_database,student_database[0].keys())
            elif option == 7:
                os.system('CLS')
                print("Hasta pronto!")
                break
            else:
                raise Exception
        except FileNotFoundError as not_found:
            os.system('CLS')
            print(f"\n\n###ATTENTION###: An error ocurred in execute_main_menu function due to no CSV file has been exported yet:{not_found}")
        except ValueError as err:
            os.system('CLS')
            print(f"\n\n###ATTENTION###:An error ocurred in execute_main_menu function due to selecting an invalid option and due to:{err}\n\n")
        except IndexError as inderr:
            os.system('CLS')
            print(f"\n\n###ATTENTION###:An error ocurred in execute_main_menu function due to unable to import empty data in database:{inderr}")
        except Exception as ex:
            os.system('CLS')
            print(f"\n\n###ATTENTION###:An error ocurred in execute_main_menu function due to selecting an invalid option and due to:{ex}\n\n")