# Desafio DIO "Criando um Sistema Bancário"
# Matheus Reis Martins
# import this


# Definindo o Menu com as operações de saque, depósito e visualizar extrato:

menu = """ 
########## MENU ##########

Selecione uma opção:

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""
# Definindo as variáveis iniciais para as operações:
saldo  = 0
limite_diario = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3

# Escolha da operação:
while True: 
    operacao = input(menu)

# Operação de Depósito:
    if operacao == '1':
        valor = float(input('Informe o valor de depósito desejado: '))
        
        if valor > 0:
            saldo += valor
            extrato += (f'Depósito de R$ {valor:.2f} foi depositado.\n')
        
        else: print('A operação falhou! o valor é inválido, verifique o valor digitado para o depósito.')

# Operação de Saque:
    elif operacao == '2':
        valor = float(input('Digite o valor de saque desejado: \n'))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite_diario
        saque_indisponivel = saques >= LIMITE_SAQUES

        if saldo_excedido: print('A Operação falhou! Saldo insuficiente!')

        elif limite_excedido: print('A Operação falhou! Limite máximo por saque é de R$ 500,00.')

        elif saque_indisponivel: print('A Operação falhou! Você atingiu a quantidade máxima de saques diários (3)')

        elif valor > 0 :
            saldo -= valor
            extrato += (f'Saque de R$ {valor:.2f} realizado.')
            saques += 1

        else: print('Operação falhou! verifique o valor digitado para saque.')

# Operação de Extrato:
    elif operacao == '3':
         print('\n ########## EXTRATO ##########')
         print(' Não foram realizadas movimentações' if not extrato else extrato)
         print(f'\n Seu saldo atual é de: R$ {saldo:.2f}.')
         print('#############################')

# Finalização:
    elif operacao == '0':
        print('########## OBRIGADO E VOLTE SEMPRE ! ##########')
        break
    
    else: print('A operação digitada é inválida, verifique as opções no menu e tente novamente.')

    # be water, my friend. 
