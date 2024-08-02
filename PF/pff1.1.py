import os
import random

def limpiar_pantalla():
    # Limpiar la pantalla, compatible con Windows y Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_contraseña():
    contraseña_correcta = "italiano2024"
    intentos = 3

    while intentos > 0:
        try:
            contraseña = input("Por favor, ingresa la contraseña para acceder a la aplicación: ")
            if contraseña == contraseña_correcta:
                print("Contraseña correcta. Acceso concedido.")
                return True
            else:
                intentos -= 1
                print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
                if intentos == 0:
                    raise ValueError("Se han agotado los intentos. Acceso denegado.")
        except ValueError as e:
            print(e)
            return False

def mostrar_contenidos():
    while True:
        print("\nContenidos de aprendizaje básicos (Nivel A1)")
        print("1. Verbo essere (ser)")
        print("2. Saludos y despedidas")
        print("3. Animales")
        print("4. Colores")
        print("5. Números")
        print("6. Oraciones cortas a traducir")
        print("0. Regresar al menú principal")
        
        while True:
            opcion = input("Selecciona una opción para ver el contenido: ")
            if opcion in ['0', '1', '2', '3', '4', '5', '6']:
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")

        if opcion == '0':
            break

        limpiar_pantalla()

        if opcion == '1':
            print("\nVerbo essere (ser):")
            print("io sono - yo soy")
            print("tu sei - tú eres")
            print("lui/lei è - él/ella es")
            print("noi siamo - nosotros somos")
            print("voi siete - vosotros sois")
            print("loro sono - ellos son")
        elif opcion == '2':
            print("\nSaludos y despedidas:")
            print("ciao - hola/adiós")
            print("arrivederci - adiós")
            print("grazie - gracias")
            print("prego - de nada")
            print("buongiorno - buenos días")
            print("buonasera - buenas tardes")
            print("buonanotte - buenas noches")
            print("scusa - perdón")
        elif opcion == '3':
            print("\nAnimales:")
            print("cane - perro")
            print("gatto - gato")
            print("uccello - pájaro")
            print("elefante - elefante")
            print("topo - ratón")
            print("mucca - vaca")
        elif opcion == '4':
            print("\nColores:")
            print("rosso - rojo")
            print("blu - azul")
            print("verde - verde")
            print("giallo - amarillo")
            print("nero - negro")
            print("bianco - blanco")
        elif opcion == '5':
            print("\nNúmeros:")
            print("uno - uno")
            print("due - dos")
            print("tre - tres")
            print("quattro - cuatro")
            print("cinque - cinco")
            print("sei - seis")
        elif opcion == '6':
            print("\nOraciones cortas a traducir:")
            print("Il mio nome è Anna - Mi nombre es Anna")
            print("Io ho un cane - Tengo un perro")
            print("Buongiorno - Buenos días")
            print("Mi chiamo Marco - Me llamo Marco")
            print("Come stai? - ¿Cómo estás?")
            print("Lei è una ragazza - Ella es una niña")
        
        input("\nPresiona Enter para regresar al menú de contenidos...")
        limpiar_pantalla()

def mostrar_introduccion():
    print("\nIntroducción y explicación de los desafíos")
    print("En esta sección encontrarás desafíos con preguntas de opción múltiple.")
    print("Por cada pregunta, se te darán varias opciones y solo una es la correcta.")
    print("Obtendrás puntos por cada respuesta correcta.")
    print("¡Buena suerte y diviértete aprendiendo italiano!")

def obtener_pregunta_respuesta(categoria):
    if categoria == 1:
        pregunta, opciones, respuesta_correcta = preguntar_essere()
    elif categoria == 2:
        pregunta, opciones, respuesta_correcta = preguntar_saludos()
    elif categoria == 3:
        pregunta, opciones, respuesta_correcta = preguntar_animales()
    elif categoria == 4:
        pregunta, opciones, respuesta_correcta = preguntar_colores()
    elif categoria == 5:
        pregunta, opciones, respuesta_correcta = preguntar_numeros()
    elif categoria == 6:
        pregunta, opciones, respuesta_correcta = preguntar_oraciones()
    return pregunta, opciones, respuesta_correcta

def preguntar_essere():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cuál es la traducción de 'io sono'?", ["a) yo soy", "b) tú eres", "c) él es"], "a"
    elif opcion == 2:
        return "¿Cuál es la traducción de 'noi siamo'?", ["a) ellos son", "b) nosotros somos", "c) vosotros sois"], "b"
    elif opcion == 3:
        return "¿Cuál es la traducción de 'tu sei'?", ["a) él es", "b) nosotros somos", "c) tú eres"], "c"
    elif opcion == 4:
        return "¿Cuál es la traducción de 'lui è'?", ["a) ella es", "b) él es", "c) tú eres"], "b"
    elif opcion == 5:
        return "¿Cuál es la traducción de 'voi siete'?", ["a) tú eres", "b) ellos son", "c) vosotros sois"], "c"
    elif opcion == 6:
        return "¿Cuál es la traducción de 'loro sono'?", ["a) ellos son", "b) nosotros somos", "c) tú eres"], "a"

def preguntar_saludos():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cómo se dice 'hola' en italiano?", ["a) ciao", "b) arrivederci", "c) grazie"], "a"
    elif opcion == 2:
        return "¿Cómo se dice 'adiós' en italiano?", ["a) buongiorno", "b) buonanotte", "c) arrivederci"], "c"
    elif opcion == 3:
        return "¿Cómo se dice 'gracias' en italiano?", ["a) prego", "b) grazie", "c) scusa"], "b"
    elif opcion == 4:
        return "¿Cómo se dice 'buenos días' en italiano?", ["a) buonanotte", "b) buongiorno", "c) buonasera"], "b"
    elif opcion == 5:
        return "¿Cómo se dice 'buenas noches' en italiano?", ["a) buonasera", "b) buongiorno", "c) buonanotte"], "c"
    elif opcion == 6:
        return "¿Cómo se dice 'por favor' en italiano?", ["a) scusa", "b) prego", "c) grazie"], "b"

def preguntar_animales():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cuál es la traducción de 'cane'?", ["a) gato", "b) perro", "c) pájaro"], "b"
    elif opcion == 2:
        return "¿Cuál es la traducción de 'gatto'?", ["a) gato", "b) elefante", "c) pájaro"], "a"
    elif opcion == 3:
        return "¿Cuál es la traducción de 'uccello'?", ["a) elefante", "b) perro", "c) pájaro"], "c"
    elif opcion == 4:
        return "¿Cuál es la traducción de 'elefante'?", ["a) elefante", "b) perro", "c) gato"], "a"
    elif opcion == 5:
        return "¿Cuál es la traducción de 'topo'?", ["a) ratón", "b) perro", "c) gato"], "a"
    elif opcion == 6:
        return "¿Cuál es la traducción de 'mucca'?", ["a) perro", "b) vaca", "c) pájaro"], "b"

def preguntar_colores():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cuál es la traducción de 'rosso'?", ["a) rojo", "b) azul", "c) verde"], "a"
    elif opcion == 2:
        return "¿Cuál es la traducción de 'blu'?", ["a) amarillo", "b) azul", "c) verde"], "b"
    elif opcion == 3:
        return "¿Cuál es la traducción de 'verde'?", ["a) rojo", "b) blanco", "c) verde"], "c"
    elif opcion == 4:
        return "¿Cuál es la traducción de 'giallo'?", ["a) amarillo", "b) azul", "c) rojo"], "a"
    elif opcion == 5:
        return "¿Cuál es la traducción de 'nero'?", ["a) blanco", "b) negro", "c) rojo"], "b"
    elif opcion == 6:
        return "¿Cuál es la traducción de 'bianco'?", ["a) negro", "b) rojo", "c) blanco"], "c"

def preguntar_numeros():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cuál es la traducción de 'uno'?", ["a) uno", "b) dos", "c) tres"], "a"
    elif opcion == 2:
        return "¿Cuál es la traducción de 'due'?", ["a) tres", "b) dos", "c) uno"], "b"
    elif opcion == 3:
        return "¿Cuál es la traducción de 'tre'?", ["a) uno", "b) tres", "c) dos"], "b"
    elif opcion == 4:
        return "¿Cuál es la traducción de 'quattro'?", ["a) cuatro", "b) cinco", "c) seis"], "a"
    elif opcion == 5:
        return "¿Cuál es la traducción de 'cinque'?", ["a) siete", "b) ocho", "c) cinco"], "c"
    elif opcion == 6:
        return "¿Cuál es la traducción de 'sei'?", ["a) seis", "b) nueve", "c) diez"], "a"

def preguntar_oraciones():
    opcion = random.randint(1, 6)
    if opcion == 1:
        return "¿Cómo se traduce 'Mi nombre es Anna'?", ["a) Io sono Anna", "b) Il mio nome è Anna", "c) Lei è Anna"], "b"
    elif opcion == 2:
        return "¿Cómo se traduce 'Tengo un perro'?", ["a) Io ho un cane", "b) Io sono un cane", "c) Tu hai un cane"], "a"
    elif opcion == 3:
        return "¿Cómo se traduce 'Buenos días'?", ["a) Buongiorno", "b) Buonasera", "c) Buonanotte"], "a"
    elif opcion == 4:
        return "¿Cómo se traduce 'Me llamo Marco'?", ["a) Il mio nome è Marco", "b) Io sono Marco", "c) Mi chiamo Marco"], "c"
    elif opcion == 5:
        return "¿Cómo se traduce '¿Cómo estás?'?", ["a) Come stai?", "b) Come sei?", "c) Chi sei?"], "a"
    elif opcion == 6:
        return "¿Cómo se traduce 'Ella es una niña'?", ["a) Lui è un ragazzo", "b) Lei è una ragazza", "c) Lei è un ragazzo"], "b"

def iniciar_desafios(nombre):
    print("\nInicio de desafíos:")
    puntaje = 0
    total_preguntas = 6
    
    for i in range(total_preguntas):
        limpiar_pantalla()
        categoria = random.randint(1, 6)
        pregunta, opciones, respuesta_correcta = obtener_pregunta_respuesta(categoria)
        
        print(f"\nPregunta {i+1}: {pregunta}")
        for opcion in opciones:
            print(opcion)
        
        while True:
            respuesta = input("Tu respuesta: ").lower()
            if respuesta in ['a', 'b', 'c']:
                break
            else:
                print("Opción no válida. Por favor, selecciona 'a', 'b' o 'c'.")

        if respuesta == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{respuesta_correcta}'.")

    print(f"\nDesafíos completados. {nombre}, tu puntaje final es: {puntaje}/{total_preguntas}")
    if puntaje == total_preguntas:
        print(f"¡Excelente, {nombre}! ¡Has respondido todas las preguntas correctamente!")
    elif puntaje >= total_preguntas / 2:
        print(f"¡Bien hecho, {nombre}! ¡Tienes un buen conocimiento básico de italiano!")
    else:
        print(f"No te preocupes, {nombre}. ¡Sigue practicando y mejorarás!")

def main():
    print("=====================================")
    print("        Bienvenido a DuoItaliano     ")
    print("     Aprendizaje básico de italiano  ")
    print("=====================================")

    if not solicitar_contraseña():
        return

    limpiar_pantalla()

    while True:
        nombre = input("Por favor, ingresa tu nombre: ").strip()
        if nombre.isalpha():
            nombre = nombre.capitalize()
            break
        else:
            print("Nombre inválido. Por favor, ingresa un nombre que contenga solo letras.")
    
    limpiar_pantalla()

    while True:
        print("\nMenú Principal")
        print("1) Contenidos de aprendizaje básicos")
        print("2) Introducción y explicación de los desafíos")
        print("3) Desafíos (ejercicios de opciones múltiples)")
        print("4) Salir")
        
        while True:
            opcion = input("Selecciona una opción: ")
            if opcion in ['1', '2', '3', '4']:
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")

        if opcion == '1':
            mostrar_contenidos()
        elif opcion == '2':
            mostrar_introduccion()
        elif opcion == '3':
            iniciar_desafios(nombre)
        elif opcion == '4':
            print(f"Gracias por jugar a DuoItaliano, {nombre}. ¡Adiós!")
            break

if __name__ == "__main__":
    main()
