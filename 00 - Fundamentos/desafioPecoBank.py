menu = """
 ###### MENU ######
 #                #
 #  [1] Deposito  #
 #  [2] Saque     #
 #  [3] Extrato   #
 #  [0] Sair      #
 #                #
 ##################
>>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  acao = input(menu)

  if acao == '1':
    valor = float(input('Digite o valor do deposito: '))

    if valor > 0:
      saldo += valor
      extrato += f'Depósito: R$ {valor:.2f}\n'
      print('Deposito realizado com sucesso!')

    else:
      print('Não foi possivel realizar o depósito, valor inválido!')

  elif acao == '2':
    valor_saque = float(input('Digite o valor de saque: '))

    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saques:
      print('Você atingiu seu limite de saques!')
    
    elif excedeu_limite:
      print('O limite para cada saque é de R$ 500,00')

    elif excedeu_saldo:    
      print('Saldo insuficiente!')

    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f'Saque: R$ {valor_saque:.2f}\n'
      numero_saques += 1
      print('Saque realizado com sucesso!')
    
    else:
      print('Operação falhou, o valor é inválido!')

  elif acao == '3':
    print('==========EXTRATO BANCÁRIO==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: {saldo:.2f}')
    print('====================================')

  elif acao == '0':
    break

  else:
    print('Por favor digite uma operação válida!')
