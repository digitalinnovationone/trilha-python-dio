frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

numeros = range(11)
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print("Números pares:", numeros_pares)

numeros = [4, 5, 7, 9]
numeros_quadrados = []
for numero in numeros:
    numeros_quadrados.append(numero ** 2)
print("Números quadrados utilizando For Loop:", numeros_quadrados)

numeros = [10, 6, 3, 2]
numeros_quadrados = [numero ** 2 for numero in numeros]
print("Números quadrados utilizando Compreensão de Listas:", numeros_quadrados)
