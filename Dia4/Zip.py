names = ['Ruperto', 'Romualdo', 'Romulo']
edades = [32, 51, 150]
ciudades = ['Lima', 'Madrid','TucumanUra']
mixed = list(zip(names,edades,ciudades))

print(mixed)

for name,age,city in mixed:
    print(f"{name} tiene {age} años y vive en {city}")