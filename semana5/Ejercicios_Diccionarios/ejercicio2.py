list_a = ["first_name","last_name","role"]
list_b = ["Kevin","Bastos","CEO"]
dictionary = {}

for index , record in enumerate(list_a):
    dictionary[list_a[index]] = list_b[index] 
print(dictionary)
