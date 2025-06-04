numeros = [1,12,10,25,70,95,12,41,40,12,15,12,10]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Os números pares são: {pares}")
print(f"Os números impares são {impares}")

