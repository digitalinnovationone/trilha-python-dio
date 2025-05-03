contas = {}

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    contas[titular] = saldo

print(", ".join([f"{chave}: R$ {valor}" for chave, valor in contas.items()]))