lista=[1,2,3,4,5,6,7,8,9,10]

for index , record in enumerate(lista):
    if lista[index] % 2 == 0:
                lista.pop(index)
print(*lista)