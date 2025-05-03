# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
cubo = [num ** 3 for num in numeros if num >= 20]
print(cubo)

quadrado = [numero**2 for numero in numeros]
print(quadrado)
