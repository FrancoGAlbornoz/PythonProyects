texto = input("Ingresa un texto: ")

letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la seguda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")

print("Cantidad de letras")

cantidadL1 = texto.count(letras[0])
cantidadL2 = texto.count(letras[1])
cantidadL3 = texto.count(letras[2])

print(f"Se encontro la letra '{letras[0]}'  repetida '{cantidadL1}' veces")
print(f"Se encontro la letra '{letras[1]}' repetida '{cantidadL2}' veces")
print(f"Se encontro la letra '{letras[2]}' repetida '{cantidadL3}' veces")

print("\n")

print("Cantidad de palabras.")
palabras = texto.split()
print(f"Se encontraron en tu texto un total de {len(palabras)}")

print("\n")
print("Letras fin e inicio")

letraI = texto[0]
letraF = texto[-1]

print(f"La letra de inicio es {letraI} y la letra final es {letraF}")

print("\n")
print("Texto invertudo")

palabras.reverse()
textoinvertido = ' '.join(palabras)

print(f"Si ordenamos tu texto al revez va a mostrar esto {textoinvertido}")

print("\n")
print("Buscar PHYTON")

buscarP = 'phyton' in texto

dic = {True: "si", False: "no"}

print(f"La palabra PHYTON '{dic[buscarP]}' esta en el texto ")