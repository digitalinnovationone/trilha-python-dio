carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")

