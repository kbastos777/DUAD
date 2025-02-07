import csv
import os

def return_list_data(file_path):
    data_collection = []
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Returning empty list.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_collection.append(list(row.values()))
        return data_collection
    except ValueError as ex:
        print(f"An error occurred in collect_data function due to {ex}")
        return []


# def return_list_data(input_list):#Esta funcion de aca le va a quitar el formato de diccionario al output y solo va a devolver los valores en formato de lista
#     try:    
#         new_list = []
#         for record in input_list:
#             new_list.append(list(record[0].values()))
#             print(list(record[0].values()))
#         return new_list
#     except TypeError as err:
#         print(f"An error ocurred in return_list_function due to {err}")


def create_dict(title_value,amount_value,category_value):
    try:
        dictionary = {}
        key = 'Title'
        dictionary[key] = title_value
        key = 'Amount'
        dictionary[key] = amount_value
        key = 'Category'
        dictionary[key] = category_value
    except ValueError as error:
        print(f"An error occurred in create_dict function due to{error}")
    return dictionary


def write_csv_file(file_path,data,headers):
    try:
        with open (file_path,'a',encoding='utf-8') as file:
                file.truncate(0) #Esto va a evitar que se repitan datos al ser sobre escritos
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                writer.writerows(data)
    except ValueError as error:
            (f"An error occurred in write_csv_file function due to {error}")


def collect_data(file_path):
    data_collection = []
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Returning empty list.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_collection.append(list(row.values()))
        return data_collection
    except ValueError as ex:
        print(f"An error occurred in collect_data function due to {ex}")
        return []


def collect_category_data(file_path):
    category_collection = []
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Returning empty list.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                    if row['Category'] not in category_collection:  # Evita duplicados
                        category_collection.append(row['Category'])
        return category_collection
    except ValueError as ex:
        print(f"An error occurred in collect_data function due to {ex}")
        return []