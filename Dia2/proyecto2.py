print("Calculadora de Comisiones")

nombre = input("Tu nombre: ")

ventas = input("Cuanto en ventas ganaste: ")

ventas = float(ventas)

cantComisiones = ventas*13/100

round(cantComisiones,2)

print(f"Hola {nombre} , tu dinero en comisiones es de {cantComisiones}")




