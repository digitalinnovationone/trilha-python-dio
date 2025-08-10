''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0
    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:  
            # TODO: Adicione o valor da transação ao saldo
        saldo += float(transacao)
    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    exibicao_saldo = f"Saldo: R$ {saldo:.2f}"
    return exibicao_saldo

entrada_usuario = input() # Exemplo: [100, -50, 200]
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(transacao) for transacao in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)