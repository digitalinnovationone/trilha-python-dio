saldo = 0
limite = 500
extrato = ''
qtd_saques = 0
contas = []
usuarios = []

AGENCIA = '0001'
LIMITE_SAQUES = 3


def menu():
    menu_texto = '''
    \t\t MENU INICIAL \t\t

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar uma nova conta
    [6] Listar o Usuário
    [0] Sair

    Digite a operação desejada: '''
    return input(menu_texto)


# depósito
def depositar(saldo, extrato):
    valor = float(input('\nInforme o valor do depósito: '))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Operação falhou! O valor informado é inválido.')

    return saldo, extrato


# saque
def sacar(saldo, extrato, limite, qtd_saques):
    valor = float(input('\nInforme o valor do saque: '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = qtd_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Operação falhou! O seu saldo é insuficiente.')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('Operação falhou! Você excedeu o limite de saques.')
    elif valor >= 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        qtd_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou! O valor informado é inválido.')

    return saldo, extrato


# extrato
def mostrar_extrato(saldo, extrato):
    print('\n\t\t\tEXTRATO\t\t\t')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo R$ {saldo:.2f}\n')


def filtro_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None


def criando_usuario(usuarios):
    cpf = input('\nInforme o CPF do usuário: ')
    usuario = filtro_usuarios(cpf, usuarios)
    
    if usuario:
        print('\tUsuário já existe!')
        return
    
    nome = input('Informe o seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o seu endereço (Rua, número, bairro - Cidade / Estado em sigla): ')

    usuarios.append({'cpf': cpf,'nome': nome, 'data de nascimento': data_nascimento, 'endereço':endereco})
    print('\tUsuário criado com sucesso! <3')
    return


def criar_conta(agencia, numeroConta, usuarios):
    cpf = input('\nInforme o CPF do usuário: ')
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print('\tConta criada com sucesso!')
        return {'agencia': agencia, 'numeroConta': numeroConta, 'usuario': usuario }
    else:
        print('Usuário não encontrado.')
    return None


def listagem(contas):
    for conta in contas:
        lista_texto = f'''
        Agência: {conta['agencia']}
        Conta(C/C): {conta['numeroConta']}
        Titular da Conta: {conta['usuario']['nome']}
        '''
        print(lista_texto)  
 



while True:
    opcao = menu()
    if opcao == '0':
        print("Saindo...")
        break

    elif opcao == '1':
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == '2':
        saldo, extrato = sacar(saldo, extrato, limite, qtd_saques)
    elif opcao == '3':
        mostrar_extrato(saldo, extrato)
    elif opcao == '4':
        criando_usuario(usuarios)
    elif opcao == '5':
        numeroConta = len(contas) + 1
        conta = criar_conta(AGENCIA, numeroConta, usuarios)
        if conta:
            contas.append(conta)    
    elif opcao == '6':
        listagem(contas)

    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')
