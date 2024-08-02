lista = ['a','b','c']


for item in enumerate(lista):
    print(item)


 #or mas formal

lista2 = ['a', 'b', 'c', 'd']

misTuples = list(enumerate(lista2))
print(misTuples[1][0])
