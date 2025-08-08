valor = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(('''    ========Menu========
                       
    Selecione uma opção:

    [1] Depositar
    [2] Sacar
    [3] Consultar Saldo
    [0] Sair

    Digite sua opção:''')))
    
    if opcao == 1:
        valor_deposito = float(input('Digite o valor a ser depositado: '))
        if valor_deposito <= 0:
            print('Valor inválido! O depósito deve ser maior que zero.')
            continue
        else:
            print(f'Você depositou R$ {valor_deposito:.2f}')
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
            valor += valor_deposito
    elif opcao == 2:
        valor_saque = float(input('Digite o valor a ser sacado: '))
        if valor_saque > valor:
            print('Saldo insuficiente!')
        elif valor_saque > limite:
            print(f'O valor do saque não pode ser maior que R$ {limite:.2f}!')
        elif numero_saques >= LIMITE_SAQUES:
            print(f'Número máximo de saques por dia é {LIMITE_SAQUES}.')
        else:
            valor -= valor_saque
            numero_saques += 1
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            print(f'Você sacou R$ {valor_saque:.2f}')
    elif opcao == 3:
        print('\n========= Extrato =========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {valor:.2f}')
        print('===========================')
    elif opcao == 0:
        print('Obrigado por utilizar nosso sistema!')
        break
    else:
        print('Opção inválida! Tente novamente.')

print('Saindo do sistema...')