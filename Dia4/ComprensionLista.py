palabra = "python"

lista = [xx for xx in "legumbre"]
print(lista)

#OR

lista2 = [n if n * 2 >10 else 'No' for n in range(0,20+1,2) ]
print(lista2)

#OR

pies = [10,20,30,40,50]

metros = [p*3.281 for p in pies]
print(metros)