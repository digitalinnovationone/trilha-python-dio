carros = ["gol", "celta", "palio","uno","corolla","fusca","brasilia","opala","vectra","fiesta"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")
