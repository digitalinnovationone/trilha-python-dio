''' 

Desafio - Gestão e Controle de Transações Bancárias - Transações Acima de um Limite

Descrição
Você foi solicitado a criar um programa que analise uma lista de transações bancárias e filtre apenas aquelas que ultrapassam um valor limite. Seu programa deve retornar uma nova lista contendo somente as transações cujo valor absoluto (ignorar sinal negativo) seja maior que o limite informado.

Atenção:
As transações incluem tanto depósitos (positivos) quanto saques (negativos).
Valor absoluto é o critério para filtrar, então tanto 300 (depósito) quanto -150 (saque) serão considerados, já que ambos têm módulo maior que 100.
Entrada
Uma lista de valores representando as transações bancárias (ex.: [100, -50, 300, -150]).
Um valor limite (inteiro ou decimal) fornecido pelo usuário.
Saída
Uma nova lista com as transações que ultrapassam o limite, no formato: "Transações: [X, Y, Z]"

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
[100, -50, 300, -150], 100	Transações: [300, -150]
[200, -50, 400], 150	Transações: [200, 400]
[1000, -75, 800], 500	Transações: [1000, 800]
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.

Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    for transacao in transacoes:
      if abs(transacao) > limite:
        transacoes_filtradas.append(transacao)
        
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)


print(f"Transações: {resultado}")