# COMPREENSAO_DE_LISTAS
# É uma forma concisa de criar listas. É uma forma de criar listas a partir de outras listas, iterando sobre elas.
# utilidade: é uma forma de criar listas de forma mais rápida e limpa.
# Sintaxe: [ <expressao> for <variavel> in <nome da lista> <if, se houver> ]

# exemplo 1
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(f"pares: {pares}")

# exemplo 2
numeros = [1,2,3,4,5,6,7,8,9,10]
impares = [numero for numero in numeros if numero % 2 != 0]
print(f"impares: {impares}")

# exemplo 3
numeros = [1,2,3,4,5,6,7,8,9,10]
quadrados = [numero**2 for numero in numeros]
print(f"quadrados: {quadrados}")

