import os
from resources.data import Bus


def main_menu ():
    os.system("CLS")
    while True:
        try:    
                school_bus = Bus()
                print("\n\nMain menu")
                print("\nOption 1: Add new passengers")
                print("Option 2: Dispatch passengers")
                print("Option 3: Exit")
                option = int(input("\nPlease select an option:"))
                if option == 1:
                    passenger = input("Please enter the passengers name:")
                    school_bus.AddPasengers(passenger,school_bus.passenger_list)
                elif option == 2:
                    school_bus.DispatchPassengers()
                elif option == 3:
                    os.system("CLS")
                    print("Good bye!")
                    break
                elif option == 4 :
                    print(f"Estos contiene la lista{school_bus.passenger_list}")
                else:
                    os.system("CLS")
                    print("Please select a valid option")
        except Exception as ex:
            print(f"An error ocurred in main_menu function due to:{ex}")