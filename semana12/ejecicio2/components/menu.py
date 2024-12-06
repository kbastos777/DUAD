import os
from components.data import Square,Circle,Rectangle


def main_menu():
    while True:
        try:    
            print("### Welcome to Shapes System ###\n\n")
            print("Option1: Calculate the circle area/perimeter")
            print("Option2: Calculate the square area/perimeter")
            print("Option3: Calculate the rectangle area/perimeter")
            print("Option4: Exit")
            option = int(input("Please select an option:"))
            if option == 1:
                circle_menu()
            elif option == 2:
                square_menu()
            elif option == 3:
                rectangle_menu()
            elif option == 4:
                os.system("CLS")
                print("Good bye!")
                break
            else:
                os.system("CLS")
                print("##Error##: Invalid option, please try again")
        except ValueError as err:
            print(f"An error occurred in main_menu method due to: {err}")


def circle_menu():
    os.system("CLS")
    circle =  Circle()
    circle.radius
    while True:
        try:    
            print("###Circle menu###\n\n")
            print("Option1:Calculate Perimeter")
            print("Option2:Calculate Area")
            print("Option3:Return to main menu")
            option = int(input("Please select an option:"))
            if option == 1:
                circle_perimeter = circle.calculate_perimeter()
                os.system("CLS")
                print(f"This Circle Perimeter is:{circle_perimeter}\n\n")
            elif option == 2:
                circle_area = circle.calculate_area()
                os.system("CLS")
                print(f"This Circle Area is:{circle_area}\n\n")
            elif option == 3:
                os.system("CLS")
                break
            else:
                os.system("CLS")
                print("##Error##: Invalid option, please try again")
        except ValueError as err:
            print(f"An error occurred in main_menu method due to: {err}")


def square_menu():
    os.system("CLS")
    square =  Square()
    square.side
    while True:    
        try:    
            print("###Square menu###\n\n")
            print("Option1:Calculate Perimeter")
            print("Option2:Calculate Area")
            print("Option3:Return to main menu")
            option = int(input("Please select an option:"))
            if option == 1:
                square_perimeter = square.calculate_perimeter()
                os.system("CLS")
                print(f"This Square Perimeter is:{square_perimeter}\n\n")
            elif option == 2:
                square_area = square.calculate_area()
                os.system("CLS")
                print(f"This Square Area is:{square_area}\n\n")
            elif option == 3:
                os.system("CLS")
                break
            else:
                os.system("CLS")
                print("##Error##: Invalid option, please try again")
        except ValueError as err:
            print(f"An error occurred in main_menu method due to: {err}")


def rectangle_menu():
    os.system("CLS")
    rectangle =  Rectangle()
    rectangle.length
    rectangle.width
    while True:
        try:
            print("###Rectangle menu###\n\n")
            print("Option1:Calculate Perimeter")
            print("Option2:Calculate Area")
            print("Option3:Return to main menu")
            option = int(input("Please select an option:"))
            if option == 1:
                rectangle_perimeter = rectangle.calculate_perimeter()
                os.system("CLS")
                print(f"This Rectangle Perimeter is:{rectangle_perimeter}\n\n")
            elif option == 2:
                rectangle_area = rectangle.calculate_area()
                os.system("CLS")
                print(f"This Rectangle Area is:{rectangle_area}\n\n")
            elif option == 3:
                os.system("CLS")
                break
            else:
                os.system("CLS")
                print("##Error##: Invalid option, please try again")
        except ValueError as err:
            print(f"An error occurred in main_menu method due to: {err}")