# Desafio DIO "Otimizando um Sistema Bancário através de funções e demais conhecimentos"
# Matheus Reis Martins
# import this



# Importar data para melhoria no extrato:
from datetime import datetime


# Definindo o Menu das operações de saque, depósito, visualizar extrato e demais novas opções como uma função:
# Definir função de menu com novas opões:
def menu() : 
    menu = """ 
########## MENU ##########

Selecione uma opção:

[1] Depósito
[2] Saque
[3] Extrato
[4] Novo Usuário 
[5] Nova Conta
[6] Encerrar Conta (em breve)
[7] Listar Contas Ativas
[0] Sair

##########################
"""
    return input(menu)   # Retornar o preenchimento do menu



# Definir função de depósito:
def deposito(saldo, valor, extrato, /):
     if valor > 0:
            saldo += valor
            extrato += (f'O depósito de R$ {valor:.2f} foi realizado em {datetime.now()} .\n')
            print(f'#### O valor de {valor:.2f} foi depositado com sucesso! #### \n') # Nova mensagem de sucesso da operação

     else: 
            print('A operação falhou! o valor é inválido, verifique o valor digitado para o depósito.')

     return saldo, extrato



# Definir função de saque:
def saque(*, valor, saldo, extrato, limite_diario, saques, LIMITE_SAQUES):

    saldo_excedido = valor > saldo
    limite_excedido = valor > limite_diario
    saque_indisponivel = saques >= LIMITE_SAQUES

    if saldo_excedido: print('A Operação falhou! Saldo insuficiente!')

    elif limite_excedido: print('A Operação falhou! Limite máximo por saque é de R$ 500,00.')

    elif saque_indisponivel: print('A Operação falhou! Você atingiu a quantidade máxima de saques diários (3)')

    elif valor > 0 :
            saldo -= valor
            extrato += (f'Saque de R$ {valor:.2f} realizado em {datetime.now()}. \n')
            saques += 1
            print(f'#### O saque de R$ {valor:.2f} foi realizado com sucesso! #### \n') # Nova mensagem de sucesso da operação

    else: print('Operação falhou! verifique o valor digitado para saque.')

    return saldo, extrato



# Definir função de extrato:
def show_extrato(saldo, /, *, extrato):

    print('\n ########## EXTRATO ##########')
    print(' Não foram realizadas movimentações' if not extrato else extrato)
    print(f'\n Seu saldo atual é de: R$ {saldo:.2f}.')
    print('#############################')



# Definir função de novo usuários:
def novo_usuario(usuarios):
     
     cpf = input(int('Por favor, digite seu CPF (somente numeros): '))
     usuario = filtro(cpf,usuarios)

     if usuario:
          print('Usuário já existente para o CPF informado!')
          return
     
     nome = input('Por favor, digite o nome completo do titular da conta: ')
     nascimento = input('Informe a data de nascimento separada por "/": ')
     endereco = input('Informe o endereço (estado (sigla), cidade, bairro, rua e numero): ')

     usuarios.append({"nome" : nome, "CPF" : cpf, "nascimento" : nascimento, "endereço" : endereco })

     print('#### Usuário criado com sucesso! ####')



# Definir o filtro para verificar se o usário já está cadastrado:
def filtro(cpf, usuarios):
     filtro_usuario = [usuario for usuario in usuarios if usuarios["cpf"] == cpf ]
     return filtro_usuario[0] if filtro_usuario else None



# Definir função para criar novos usuários:
def criar_conta(agencia, conta, usuarios):
     cpf = input('Informe o CPF para criação da conta (somente números): ')
     usuario = filtro(cpf, usuarios)

     if usuario:
          print('#### Conta criada com sucesso! ####')
          return {"Agência": agencia, "Conta" : conta, "Usuário" : usuario}
     
     print('ERRO! Usuários não encontrado, verifique o usuário!')



def listar(contas):
     for n_conta in contas:
          linha = f""" \
             Agência: {n_conta["Agência"]}
             CC: {n_conta["Conta"]}
             Titular : {n_conta["Usuário"]["nome"]}

          """
          print("=" * 100)
          print(linha)


#def encerrar(agencia, conta, usuarios):
     

def main():
# Definindo as variáveis iniciais para as operações:
    saldo = 0
    limite_diario = 500
    extrato = ""
    saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = '0001'



# Escolha da operação:
    while True: 
        operacao = menu()

# Operação de Depósito:
        if operacao == '1':
            valor = float(input('Informe o valor de depósito desejado: '))

            saldo, extrato = deposito(saldo, valor, extrato)

# Operação de Saque:
        elif operacao == '2':
            valor = float(input('Digite o valor de saque desejado: \n'))

            saldo, extrato = saque(
                 saldo = saldo,
                 valor = valor,
                 extrato = extrato,
                 limite_diario = limite_diario,
                 saques = saques,
                 LIMITE_SAQUES = LIMITE_SAQUES,          

            )

# Operação de Extrato:
        elif operacao == '3':
             show_extrato(saldo, extrato=extrato)
             
# Operação de Novo Usuário:
        elif operacao == '4':
             novo_usuario(usuarios)
             
# Operação de Nova Conta:
        elif operacao == '5':
             conta = len(contas) + 1
             n_conta = criar_conta(AGENCIA, conta, usuarios)

             if n_conta:
                  contas.append(n_conta)


# Operação de Extrato:
        elif operacao == '6':
             print('Opção estará disponível em breve, aguarde!')


# Finalização:
        elif operacao == '7':
            listar(contas)


# Operação de Extrato:
        elif operacao == '0':
             print('Obrigado pro utilizar o sistema! Volte sempre!')

             break            

        else: print('A operação digitada é inválida, verifique as opções no menu e tente novamente.')

    # be water, my friend. 

main()
