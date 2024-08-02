"""coins = 5

while coins > 0:
    print(f"Tengo {coins} monedas")
    coins-=1
else:
    print("NO MAS MONEDAS")"""

'''respuesta ='s'

while respuesta == 's':
    respuesta = input("Desea continuar? s/n")
else:
    print("Thanks")'''

# Pass: NO ALTERA AL PROGRAMA, OCUPA UN LUGAR DONDE SE ESPERA UNA DECLARACION
'''respuesta ='s'

while respuesta == 's':
    pass

print("Hola")'''

# Break: SE PRODUCE LA SALIDA DEL BUCLE Y EN ALGUNOS CASOS DEL PROGRAMA
name = input("Tu nombre?")

for letra in name:
    if letra == 'r':
        break

# Continue: INTERRUMPE LA ITERACION ACTUAL DEL BUCLE, REINICIANDO EL BUCLE.

for letra in name:
    if letra == 'r':
        continue
    print(letra)
