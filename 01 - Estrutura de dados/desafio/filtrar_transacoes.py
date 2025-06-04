''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
    
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite:
            # TODO: Adicione a transação à lista filtrada:
            transacoes_filtradas.append(transacao)
    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")