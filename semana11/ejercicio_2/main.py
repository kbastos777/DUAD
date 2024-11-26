from resources.menu import main_menu

def main():
    try:
        main_menu()
    except Exception as ex:
        print(f"An error ocurred in main method due to: {ex}")


main()