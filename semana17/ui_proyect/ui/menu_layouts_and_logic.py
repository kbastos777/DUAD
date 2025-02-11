from ui_utilities.data_utilities import create_dict,write_csv_file,collect_data,return_list_data,return_category_data,create_category_dict,collect_category_data
import PySimpleGUI as sg
import os


sg.theme('Dark Green 2')
headings_database = [["Title"],["Amount"],["Category"]]
financial_data = return_list_data('data.csv')
print(f"[DEBUG] initializing financial_data: {financial_data }")
category_database = return_category_data('categories.csv')


def create_main_layout():
    main_layout = [
        [sg.Push(),sg.Text("Welcome to the personal budget administrator",font=("Terminal", 24)),sg.Push()],
        [sg.Push(),sg.Table(values=collect_data('data.csv'), headings=headings_database, max_col_width=25, background_color='lightblue',
                        auto_size_columns=False,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        tooltip='Income and Expenses table'),sg.Push()],
        [sg.Push(),sg.Text("Please select an option",font=("Terminal", 15)),sg.Push()],
        [sg.Push(),sg.Button("Add Income"), sg.Button("Add Expense"), sg.Button("Add Category"),sg.Push()],
    ]
    return main_layout


def create_category_layout():
    expense_layout = [
        [sg.Push(),sg.Text("Create a category",font=("Terminal", 24)),sg.Push()],
        [sg.Push(),sg.Text("Please enter the category name",font=("Terminal", 15)),sg.Push()],
        [sg.Push(),sg.Input(key="-CATEGORY-"),sg.Push()],
        [sg.Push(),sg.Button("Accept"), sg.Button("Cancel"),sg.Push()],
    ]
    return expense_layout


def create_income_layout(categories):
    income_layout =  [
        [sg.Push(), sg.Text("Income Records", font=("Terminal", 24)), sg.Push()],
        [sg.Push(), sg.Text("Please enter the income record", font=("Terminal", 15)), sg.Push()],
        [sg.Push(), sg.Text("Title"),sg.Input(key="-TITLE-"), sg.Push()],
        [sg.Push(), sg.Text("Amount"),sg.Input(key="-AMOUNT-"), sg.Push()],
        [sg.Push(), sg.Text("Select a Category "),sg.Combo(categories, key="-MY_CATEGORY-", readonly=True), sg.Push()],
        [sg.Push(), sg.Button("Accept"), sg.Button("Cancel"), sg.Push()],
    ]
    return income_layout


def create_expense_layout(categories):
    expense_layout = [
        [sg.Push(), sg.Text("Expense Records", font=("Terminal", 24)), sg.Push()],
        [sg.Push(), sg.Text("Please enter the expense record", font=("Terminal", 15)), sg.Push()],
        [sg.Push(), sg.Text("Title"),sg.Input(key="-TITLE-"), sg.Push()],
        [sg.Push(), sg.Text("Amount"),sg.Input(key="-AMOUNT-"), sg.Push()],
        [sg.Push(), sg.Text("Select a Category "),sg.Combo(categories, key="-MY_CATEGORY-", readonly=True), sg.Push()],
        [sg.Push(), sg.Button("Accept"), sg.Button("Cancel"), sg.Push()],
    ]
    return expense_layout


def category_logic(category_window_active):
    try:    
        category_window_active == True
        create_category_layout()
        category_window = sg.Window("Category administrator", create_category_layout())
        while True:
            eventCategory, valuesCategory = category_window.read(timeout=100)
            if eventCategory == sg.WIN_CLOSED or eventCategory == "Cancel":
                category_window.Close()
                category_window_active = False
                break
            elif eventCategory == "Accept":
                category = valuesCategory["-CATEGORY-"]
                if category and not os.path.exists('categories.csv'):
                    category_database.append(create_category_dict(category))
                    write_csv_file('categories.csv',category_database,category_database[0].keys())
                    sg.popup(f"Category '{category}' added successfully!")
                    category_window.Close()
                    category_window_active = False
                    break
                if category and os.path.exists('categories.csv'):
                    category_database.append(create_category_dict(category))
                    write_csv_file('categories.csv',category_database,category_database[0].keys())
                    sg.popup(f"Category '{category}' added successfully!")
                    category_window.Close()
                    category_window_active = False
                    break
    except TypeError as err:
        print(f"An error occurred in category_logic function due to {err} ")
    except ValueError as ex:
        print(f"An error occurred in category_logic function due to {ex} ")


def income_logic(income_window_active,window):
    try:    
        while True:
            income_window_active == True
            income_window = sg.Window("Income administrator", create_income_layout(collect_category_data('categories.csv')))      
            while True:
                eventIncome, values_income = income_window.read(timeout=100)
                try:  
                    if eventIncome == sg.WIN_CLOSED or eventIncome == "Cancel":
                        income_window.close()
                        income_window_active = False
                        break
                    elif eventIncome == "Accept":
                        income = values_income["-TITLE-"]
                        amount = int(values_income["-AMOUNT-"])
                        category = values_income["-MY_CATEGORY-"]
                        if income and amount and category and not os.path.exists('data.csv'):  
                            financial_data.append(create_dict(income,"+"+str(amount),category))
                            sg.popup(f"Income '{income}' added successfully!")
                            write_csv_file('data.csv', financial_data,financial_data[0].keys())
                            window["-TABLE-"].update(values=collect_data('data.csv'))
                            income_window.close()
                            income_window_active = False
                        elif income and amount and category and os.path.exists('data.csv'):
                            financial_data.append(create_dict(income,"+"+str(amount),category))
                            sg.popup(f"Income '{income}' added successfully!")
                            write_csv_file('data.csv',financial_data,financial_data[0].keys())
                            window["-TABLE-"].update(values=collect_data('data.csv'))
                            income_window.close()
                            income_window_active = False
                        elif not category:
                            sg.PopupError("Unable to add income due to missing category!")
                            if eventIncome == sg.WIN_CLOSED or eventIncome == "Cancel":
                                income_window.close()
                                income_window_active = False
                                break
                except ValueError as ex:
                    print(f"An error occurred in inner section from income_logic function due to {ex} ")
                    sg.PopupError("Invalid value type was entered on amount field, please enter a number!")
                    income_window.refresh()
                except TypeError as err:
                    print(f"An error occurred in inner section from income_logic function due to {err} ")
            break
    except TypeError as err:
        print(f"An error occurred in income_logic function due to {err} ")
    except ValueError as ex:
        print(f"An error occurred in income_logic function due to {ex} ")


def expense_logic(expense_window_active,window):
    try:    
        while True:
            expense_window_active == True
            expense_window = sg.Window("Expense administrator", create_expense_layout(collect_category_data('categories.csv')))      
            while True:
                eventExpense, values_expense = expense_window.read(timeout=100)
                try:  
                    if eventExpense == sg.WIN_CLOSED or eventExpense == "Cancel":
                        expense_window.close()
                        expense_window_active = False
                        break
                    elif eventExpense == "Accept":
                        expense = values_expense["-TITLE-"]
                        amount = int(values_expense["-AMOUNT-"])
                        category = values_expense["-MY_CATEGORY-"]
                        if expense and amount and category and not os.path.exists('data.csv'):  
                            financial_data.append(create_dict(expense,-amount,category))
                            sg.popup(f"Expense '{expense}' added successfully!")
                            write_csv_file('data.csv', financial_data,financial_data[0].keys())
                            window["-TABLE-"].update(values=collect_data('data.csv'))
                            expense_window.close()
                            expense_window_active = False
                        elif expense and amount and category and os.path.exists('data.csv'):
                            financial_data.append(create_dict(expense,-amount,category))
                            sg.popup(f"Expense '{expense}' added successfully!")
                            write_csv_file('data.csv',financial_data,financial_data[0].keys())
                            window["-TABLE-"].update(values=collect_data('data.csv'))
                            expense_window.close()
                            expense_window_active = False
                        elif not category:
                            sg.PopupError("Unable to add expense due to missing category!")
                            if eventExpense == sg.WIN_CLOSED or eventExpense == "Cancel":
                                expense_window.close()
                                expense_window_active = False
                                break
                except ValueError as ex:
                    print(f"An error occurred in inner section from expense_logic function due to {ex} ")
                    sg.PopupError("Invalid value type was entered on amount field, please enter a number!")
                    expense_window.refresh()
                except TypeError as err:
                    print(f"An error occurred in inner section from expense_logic function due to {err} ")
            break
    except TypeError as err:
        print(f"An error occurred in expense_logic function due to {err} ")
    except ValueError as ex:
        print(f"An error occurred in expense_logic function due to {ex} ")

