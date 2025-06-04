def menu():
    menu_texto = '''\n
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[n] Nova conta
[c] Cadastrar cliente
[l] Listar contas
[q] Sair
=========================

=> '''
    return input(menu_texto)

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
AGENCIA = "0001"
LIMITE_SAQUES = 3
clientes = []
contas = []
numero_conta = 1  # Contador para gerar números de conta sequenciais

def depositar(saldo, extrato):
    print("Depositar")
    valor = float(input("Informe o valor do depósito: "))
    if valor <= 0: 
        print("Operação não permitida! Informe um valor válido")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    print("Sacar")
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:  # Excedeu o saldo
        print("Saldo insuficiente!")
    elif numero_saques >= LIMITE_SAQUES:  # Excedeu a quantidade de saques
        print("Limite diário de saques atingido!")
    elif valor > limite:  # Excedeu o limite diário de saque
        print("Limite de saque excedido!")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("========== Extrato =========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("============================")
    return saldo, extrato

def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Erro: CPF já cadastrado!")
            return clientes

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/UF): ")

    clientes.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"Cliente {nome} cadastrado com sucesso!")
    return clientes

def nova_conta(clientes, contas, AGENCIA, numero_conta):
    cpf = input("Informe o CPF do cliente: ")
    cliente_encontrado = None

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Erro: Cliente não encontrado!")
        return contas, numero_conta

    conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "cliente": cliente_encontrado
    }
    contas.append(conta)
    print(f"Conta {numero_conta} cadastrada para o cliente {cliente_encontrado['nome']} com sucesso!")
    return contas, numero_conta + 1

def listar_contas(contas):
    print("========== Contas =========")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Cliente: {conta['cliente']['nome']}")
    print("============================")

    return

while True:
    opcao = menu()
    if opcao == "d" or opcao == "D":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s" or opcao == "S":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

    elif opcao == "e" or opcao == "E":
        saldo, extrato = exibir_extrato(saldo, extrato)

    elif opcao == "n" or opcao == "N":
        contas, numero_conta = nova_conta(clientes, contas, AGENCIA, numero_conta)

    elif opcao == "c" or opcao == "C":
         clientes = cadastrar_cliente(clientes) 

    elif opcao == "l" or opcao == "L":
        listar_contas(contas)      

    elif opcao == "q" or opcao == "Q":
        print("Saindo da aplicação...")
        break                     
    else:
        print("Opção inválida!")     