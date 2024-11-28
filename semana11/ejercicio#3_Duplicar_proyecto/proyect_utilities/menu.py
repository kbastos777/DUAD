import os
from proyect_utilities.actions import return_json_format,top_three_best_students,show_student_averages,Student,convert_list_to_dict
from proyect_utilities.data import write_csv,rewrite_csv


def print_main_menu_options ():
    print("\n\n##### Welcome to the student database system ######## \n\n")
    print("Main Menu")
    print("Option 1: Add new students")
    print("Option 2: Display students complete data")
    print("Option 3: See top 3 best students")
    print("Option 4: List student averages")
    print("Option 5: Export student database to a CSV file")
    print("Option 6: Import new data to CSV")
    print("Option 7: Exit\n\n")


def execute_main_menu ():
    os.system('CLS')
    student_database = []
    student_information =[]
    counter = 1
    while True:
        try:
            print_main_menu_options()
            option = int(input("Please select an option:"))
            if option == 1:
                quantity=int(input("Please enter the number of students:"))
                while counter <= quantity:
                    student = Student()#Student object instead of dictionary
                    student_information = student.create_student_list_info(student.name,student.section,student.spanish_score,student.english_score,student.social_studies_score,student.science_score)
                    student_database.append(student_information)
                    counter = counter + 1
            elif option == 2:
                os.system('CLS')
                print("\n\n\n###Students info list###\n\n")
                print(return_json_format(student_database))
            elif option == 3:
                top_three_best_students(student_database)
            elif option == 4:
                show_student_averages(student_database)
            elif option == 5:
                new_dict = convert_list_to_dict(student_database)
                print(new_dict)
                write_csv('Base_de_datos_estudiantil.csv',new_dict,new_dict[0].keys())
            elif option == 6:
                rewrite_csv('Base_de_datos_estudiantil.csv',new_dict,new_dict[0].keys())
            elif option == 7:
                os.system('CLS')
                print("Good bye!")
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