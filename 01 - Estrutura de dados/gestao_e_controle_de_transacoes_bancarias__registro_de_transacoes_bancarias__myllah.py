''' 

Desafio - Gestão e Controle de Transações Bancárias - Registro de Transações Bancárias

Descrição
Imagine que você trabalha no setor de TI de um banco e precisa criar um programa que registre as transações de uma conta bancária. Cada transação pode ser um depósito ou um saque, e todas elas serão armazenadas em uma lista. Seu programa deve calcular o saldo final da conta com base nas transações realizadas. Depósitos serão representados como valores positivos e saques como valores negativos.

Entrada
Uma lista contendo valores inteiros ou decimais representando as transações realizadas (ex.: [100, -50, 200]).

Valores positivos representam depósitos.
Valores negativos representam saques.
Saída
O saldo final da conta no formato: "Saldo: R$ X.XX"

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
[100, -50, 200]	Saldo: R$ 250.00
[500, -200, -100]	Saldo: R$ 200.00
[250 -150, -50]	Saldo: R$ 50.00
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.

Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''


def calcular_saldo(transacoes):
    saldo = 0
    
    for transacao in transacoes:
      saldo = saldo + transacao
    
    return_message = f"Saldo: R$ {format(saldo, '.2f')}"
    
    return return_message
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

resultado = calcular_saldo(transacoes)

print(resultado)