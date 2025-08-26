# Filtrar lista (1) - Comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(f"Pares: {pares}")
print(f"Impares: {impares}")

# Filtrar lista (2)
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Pares: {pares}")
print(f"Impares: {impares}")

# Modificar valores (1)
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# Modificar valores (2)
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero**2)
print(quadrado)