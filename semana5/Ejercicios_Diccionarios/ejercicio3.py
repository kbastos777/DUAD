list_of_keys = ['access_level', 'age']
employee = {'name':'Kevin',
'email':'kevin@gmail.com',
'access_level': 5, 
'age':29
}

for record in list_of_keys:
    employee.pop(record)
print(employee)