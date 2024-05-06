import datetime

menu_msg = '''
Digite uma das opções:

1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair

'''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    deposito_msg = f'''
Deposito escolhido, para voltar ao menu digite 0.
Seu saldo atual é {saldo:.2F} reais.
Insira o valor que deseja depositar:
'''
    saque_msg =f'''
Saque escolhido, para voltar ao menu digite 0.
Seu saldo atual é R${saldo:.2F}.
Seu limite de saque é R${limite:.2F}.
Digite o valor que deseja sacar:
'''
    extrato_msg =''''''

    
    opcao = input(menu_msg)

    if opcao == '1':
        while True:
            deposito_msg = f'''
Deposito escolhido, para voltar ao menu digite 0.
Seu saldo atual é R${saldo:.2F} .
Insira o valor que deseja depositar:
'''
            quantia = input(deposito_msg)
            quantia = quantia.replace(',','.')
            quantia = float(quantia) 
            if quantia > 0:
                saldo += quantia
                print('Deposito concluido com sucesso!')
                print(f'\nSeu saldo atual é R${saldo:.2F}\n')
                data_transacao = datetime.datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
                extrato.append(['Deposito',quantia,data_transacao])
                outro_deposito = input('Deseja fazer outro deposito: \n1 - Sim \nPara voltar ao menu digite qualquer outro valor\n')
                if outro_deposito == '1':
                    pass
                else:
                    break
            elif quantia == 0:
                break
            else: 
                print(f'\nDigite um valor valido!')

    elif opcao == '2':
        while True:
            saque_msg =f'''
Saque escolhido, para voltar ao menu digite 0.
Seu saldo atual é R${saldo:.2F}.
Seu limite de saque é R${limite:.2F}.
Digite o valor que deseja sacar:
'''
            quantia = input(saque_msg)
            quantia = quantia.replace(',','.')
            quantia = float(quantia) 
            if quantia > 0:
                if quantia <= limite:
                    if numero_saques < LIMITE_SAQUES:
                        if quantia <= saldo:
                                saldo -= quantia
                                limite -= quantia
                                numero_saques +=1
                                print('Saque concluido com sucesso!')
                                print(f'\nSeu saldo atual é R${saldo:.2F}\n')
                                data_transacao = datetime.datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
                                extrato.append(['Saque',quantia,data_transacao])
                                outro_saque = input('Deseja fazer outro saque: \n1 - Sim \nPara voltar ao menu digite qualquer outro valor\n')
                                if outro_saque == '1':
                                    pass
                                else:
                                    break
                        else:
                            print('\nSaldo insuficiente!\n')
                            pass
                    else:
                        print('\nQuantidade de saque diarios atingidos, tente novamente amanhã!\n')
                        pass
                else:
                    print('\nLimite de saque insuficiente!\n')
                    pass
            else:
                break

    elif opcao == '3':
        while True:
            print(extrato_msg)
            for ext in extrato:
                print(f'Movimento: {ext[0]}',end=' - ')
                print(f'Valor: R${ext[1]:.2F}',end=' - ')
                print(f'Data: {ext[2]}')
            
            if input('Aperte qualquer tecla para sair:') :
                break

    elif opcao == '0':
        print('Volte sempre!')
        break
    else:
         print('Escolha uma opção valida.')
         
