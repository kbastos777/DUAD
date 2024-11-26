import os
import csv


def write_csv(file_path , data, headers):
    
    with open(file_path,'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
    print("Operacion realizada con exito!")


#def read_csv_file (file_path):
#    os.system('CLS')
#    with open (file_path, 'r') as file:
#        reader = csv.DictReader(file)
#        for row in reader:
#            print(row)


def rewrite_csv(file_path , data, headers):
    os.system('CLS')
    with open(file_path,'a',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writerows(data)
    print("Operacion realizada con exito!")