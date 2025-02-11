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
                data_collection.append(row)
                print(f"[DEBUG] Return_list_data_ data after writing: {data_collection}")
        return data_collection
    except ValueError as ex:
        print(f"An error occurred in collect_data function due to {ex}")


def return_category_data(file_path):
    category_collection = []
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Returning empty list.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_collection.append(row)
                print(f"[DEBUG] return_category_data_ data after writing: {category_collection}")
        return category_collection
    except ValueError as ex:
        print(f"An error occurred in return_category_data function due to {ex}")


def create_dict(title_value,amount_value,category_value):
    try:
        return {
            'Title': title_value,
            'Amount': amount_value,
            'Category': category_value
        }
    except ValueError as error:
        print(f"An error occurred in create_dict function due to{error}")
        return {}


def create_category_dict(category_value):
    try:
        return {
            'Category': category_value
        }
    except ValueError as error:
        print(f"An error occurred in create_category_dict function due to{error}")
        return {}


def write_csv_file(file_path,data,headers):
    try:
        with open (file_path,'a',encoding='utf-8') as file:
                file.truncate(0) #Esto va a evitar que se repitan datos al ser sobre escritos
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                print(f"[DEBUG] write_csv_file Data before writing: {data}")
                writer.writerows(data)
    except ValueError as error:
            print(f"An error occurred in write_csv_file function due to {error}")
            return []


def collect_data(file_path):
    data_collect = []
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Returning empty list.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_collect.append(list(row.values()))
        return data_collect
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