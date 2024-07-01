# Cria uma lista vazia para armazenar os equipamentos
itens = []

# Loop para solicitar até 3 itens ao usuário
for _ in range(3):
    # Solicita o item e armazena na variável "item"
    item = input("Digite o nome do equipamento: ")
    
    # Adiciona o item à lista "itens"
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")