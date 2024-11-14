import os
import json


def add_student_data (counter):
    os.system('CLS')
    student_dict = {}
    try:
        
        name = input(f"Ingrese el nombre completo del estudiante #{counter}:")
        student_dict["nombre completo"] = name
        section = input("Ingrese la seccion del estudiante:")
        student_dict["Seccion"] = section
        

        spanish_note = int(input("Ingrese la nota en la materia de espanol:"))
        while spanish_note > 100 or spanish_note < 0:
            spanish_note = int(input("###Error###:Nota invalida, porfavor ingrese la nota en la materia de espanol:"))
        student_dict["Nota de Espanol"] = spanish_note
        

        english_note = int(input("Ingrese la nota en la materia de ingles:"))
        while english_note > 100 or english_note < 0:
            english_note = int(input("###Error###:Nota invalida, porfavor ingrese la nota en la materia de ingles:"))
        student_dict["Nota de Ingles"] = english_note
        

        social_studies_note = int(input("Ingrese la nota en la materia de estudios sociales:"))
        while social_studies_note > 100 or social_studies_note < 0:
            social_studies_note = int(input("###Error###:Nota invalida, porfavor ingrese la nota en la materia de estudios sociales:"))
        student_dict["Nota de Estudios Sociales"] = social_studies_note
        

        science_note = int(input("Ingrese la nota en la materia de ciencias:"))
        while science_note > 100 or science_note < 0:
            science_note = int(input("###Error###:Nota invalida, porfavor ingrese la nota en la materia de ciencias:"))
        student_dict["Nota de Ciencias"] = science_note
        student_dict["Promedio"] = calculate_average_note(student_dict["Nota de Espanol"],student_dict["Nota de Ingles"],student_dict["Nota de Estudios Sociales"],student_dict["Nota de Ciencias"])
        print("Registro realizado con exito!")
    except ValueError as error:
        print(f"An invalid input was entered in 'add_student_data' function, the reason for this failure is due to: {error}")
    return student_dict


def calculate_average_note(note_one,note_two,note_three,note_four):
    try:
        return(note_one + note_two + note_three + note_four)/4
    except ValueError as error:
        print(f"An error ocurred in calculate_average_note due to {error}")


def top_three_best_students(input_list):
    os.system('CLS')
    print("\n\n\n###TOP 3 Mejores promedios###\n\n")
    best_average = 0
    second_average = 0
    third_average = 0
    best_student = ''
    second_student = ''
    third_student = ''
    try:    
        for index , record in enumerate(input_list):
            current_average =  record["Promedio"]
            if current_average > best_average and current_average > second_average and current_average > third_average:
                if(best_average < current_average):
                    if second_average > third_average:
                        third_average = second_average
                        third_student = second_student
                    second_average = best_average
                    second_student = best_student
                best_average = current_average
                best_student = record["nombre completo"]
                
            elif current_average < best_average and current_average > second_average and current_average > third_average:
                if second_average > third_average:
                    third_average = second_average
                    third_student = second_student
                second_average = current_average
                second_student = record["nombre completo"]
            elif current_average < best_average and current_average < second_average and current_average > third_average:
                third_average = current_average
                third_student = record["nombre completo"]
            
        print(f"El mejor promedio es {best_student} con nota {best_average}, el segundo mejor promedio es {second_student} con nota {second_average} y el tercer mejor promedio es {third_student} con nota {third_average}")
    except ValueError as error:
        print(f"An error ocurred in top_three_best_students function due to:{error}")
    except IndexError as inderr:
        print(f"An error ocurred in top_three_best_students function due to:{inderr}")


def show_student_averages(input_list):
    os.system('CLS')
    try:
        print("\n\n\n###Lista de promedios segun el estudiante###\n\n")
        for index , record in enumerate(input_list):
            student = record["nombre completo"]
            current_average = record["Promedio"]
            print(f"\n* {student} con promedio de {current_average}")
    except IndexError as indxerr:
        print(f"An error ocurred in show_student_averages function due to:{indxerr}")    


def return_json_format(some_input):
        return json.dumps(some_input , indent=4)