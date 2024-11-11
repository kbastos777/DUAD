lista=[1,2,3,4,5]

for index , record in enumerate(lista):
    if index == lista.index(lista[0]):
            lista.insert(len(lista)-1,lista.pop(0))
            lista.insert(0,lista.pop(len(lista)-2))
print(*lista)