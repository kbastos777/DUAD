from ui.menu_layouts_and_logic import category_logic,income_logic,expense_logic,create_main_layout
import PySimpleGUI as sg


def menu_selection():
    try:
        income_window_active = False
        expense_window_active = False
        category_window_active = False
        # Create windows
        window = sg.Window("Budget Administrator", create_main_layout())
        
        while True:   
            event, values = window.read(timeout=100)
            if event == sg.WIN_CLOSED:
                break
            elif event == "Add Category" and not category_window_active:
                category_logic(category_window_active)
            elif event == "Add Income" and not income_window_active:
                income_logic(income_window_active,window)
            elif event == "Add Expense" and not expense_window_active:
                expense_logic(expense_window_active,window)
    except Exception as err:
        print(f"An error occurred in menu_selection function due to {err}")
        
