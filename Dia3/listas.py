mi_lista = ['a', 'b', 'c']
otra_lista = ['Hola', 55, 3.14]

resultado = len(mi_lista)

resultado2 = mi_lista[0:2]

print(resultado)
print(resultado2)

print(mi_lista+otra_lista)

lista3 = mi_lista+otra_lista

"""
lista3[0] = 'alfa'
print(lista3)

#lista3.append('g')
lista3.pop(0)

deleted = lista3.pop(1)

print(lista3)
print(deleted)"""

lista4 = ['k','t','y','a','l','0','v','3']

#newlista = lista4.sort()

lista4.sort()
lista4.reverse()

print(lista4)