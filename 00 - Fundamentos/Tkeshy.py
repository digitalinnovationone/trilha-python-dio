menu = """

==============menu==============

              [d] Deposito
              [s] Saque
              [e] Extrato
              [q] Sair

              => """

saldo   = 0
limite  = 500
extrato = ''
numero_de_saques = 1 #registrar o numero de saques 
LIMITE_DIARIOSAQ = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        print('Depósito')
        deposito = float(input('Digite o valor: '))
        if deposito > 0:
            saldo += deposito #acrescenta o deposito ao meu saldo
            extrato += f'Deposito: R$ {deposito:.2f}'
        else:
            print('Operação invalida, digite um valor válido.')
    elif opcao == 's':
        print('Saque')
        saque = float(input('Digite o valor: '))
        excedeu_limitesq = saque > limite
        execedeu_limite_diario = numero_de_saques > LIMITE_DIARIOSAQ
        semsaldo = saque > saldo
        if excedeu_limitesq:
            print('Excedeu limite de saque que é de R$ 500 ')
        elif execedeu_limite_diario:
            print(f'Você excedeu o limite de saques diários que é {LIMITE_DIARIOSAQ}')
        elif semsaldo:
            print('Sem saldo em conta!')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saldo: R$ {saque:2f}'
            numero_de_saques += 1
        else:
            print('Digite um valor válido')
    elif opcao == 'e':
        print('==================EXTRATO================')
        print('Não houve transições') if not extrato else extrato
        if deposito > 0:
            print (f'Deposito: R$ {deposito:.2f}')
        else:
            print('Deposito: R$ 0')
        print(f'Saldo: R$ {saldo:.2f}')
        print('===========================================')
    elif opcao == 'q':
        break


