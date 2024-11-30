import os
from utilities.menu import main_menu


def main ():
    try:
        main_menu()
    except Exception as ex:
        os.system("CLS")
        print(f"An error occurred due to {ex}")

main()