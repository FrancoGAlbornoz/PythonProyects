# Colores ANSI
rojo = '\033[91m'
verde = '\033[92m'
fin = '\033[0m'

# Pregunta 1
print("¿Cuál es el mejor tipo de alimentacion")
print("1. Omnívoro\n2. Vegetariano\n3. Vegano\n4. Otro")
respuesta = int(input("Elige una opción (1-4): "))
if respuesta == 1:
    print(f"{verde}Respuesta correcta{fin}")
else:
    print(f"{rojo}Respuesta incorrecta{fin}")
print()

# Pregunta 2
print("¿Cuántas comidas se realizan al día?")
print("1. 1-2\n2. 3-4\n3. 5-6\n4. Más de 6")
respuesta = int(input("Elige una opción (1-4): "))
if respuesta == 2:
    print(f"{verde}Respuesta correcta{fin}")
else:
    print(f"{rojo}Respuesta incorrecta{fin}")
print()

# Pregunta 3
print("¿Es saludable consumir demasiada azucar y grasas?")
print("1. Sí\n2. No")
respuesta = int(input("Elige una opción (1-2): "))
if respuesta == 2:
    print(f"{verde}Respuesta correcta{fin}")
else:
    print(f"{rojo}Respuesta incorrecta{fin}")
print()

# Pregunta 4
print("¿Es recomendable omitir el desayuno?")
print("1. Sí\n2. No")
respuesta = int(input("Elige una opción (1-2): "))
if respuesta == 2:
    print(f"{verde}Respuesta correcta{fin}")
else:
    print(f"{rojo}Respuesta incorrecta{fin}")
print()

# Pregunta 5
print("¿Debes consumir chocolates y golosinas en tu dieta diaria?")
print("1. Sí\n2. No")
respuesta = int(input("Elige una opción (1-2): "))
if respuesta == 2:
    print(f"{verde}Respuesta correcta{fin}")
else:
    print(f"{rojo}Respuesta incorrecta{fin}")
print()