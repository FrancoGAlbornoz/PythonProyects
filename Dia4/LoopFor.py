names = ['Juan', 'Franco', 'Lu', 'Katya']

'''for nombres in names:
    cnombres= names.index(nombres)+1
    print(f"Nombre {cnombres}: " + nombres)'''

'''for nombres in names:
    if nombres.startswith('L'):
        print(nombres)
    else:
        print("No")'''

'''numeros =[1,2,3,4,5]
valor=0
for numero in numeros:
    valor=valor+numero
    print(valor)'''

'''word = "python esta piola"
for letra in word:
    print(letra)

for letras in '  Python ':
    print(letras)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)'''

dic = {'clave1': 'a', 'clave2':'b', 'claves':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)