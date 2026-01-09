import re

def deposito(saldo):
    extrato = ""
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(saldo):
    extrato = ""
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    valor = float(input("Informe o valor do saque: "))
    
    if valor > (saldo + limite):
        print("Operação falhou! Você não tem saldo suficiente.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Armazenar os clientes em uma lista
# Cliente: nome, data de nascimento, cpf e endereço(logradouro, nº - bairro - cidade/UF)
# CPF: deve ser armazenado somente os números
# Não aceitar 2 clientes para o mesmo CPF
def cadastrar_cliente(dicionario_clientes):
    cpf = input("Informe o CPF do cliente: ")
    cpf = re.sub(r'\D', '', cpf)  # Remove tudo que não é número

    if cpf == "":
        print("O CPF do cliente é uma informação obrigatória!")
    else:
        # Testa se o cliente já possui cadastro
        if cpf in dicionario_clientes:
            print(f"O cliente: {dicionario_clientes[cpf]["nome"]} CPF: {cpf} já possui cadastro!")
        else:
            while True:
                nome = input("Informe o nome do cliente: ")
                nome = nome.strip()
                if nome == "":
                    print("O nome do cliente é uma informação obrigatória!")
                else:
                    break
    
            data_nascimento = input("Informe a data de nascimento do cliente: ")
            rua = input("Endereço - Informe a rua: ")
            numero = input("Endereço - Informe o número: ")
            bairro = input("Endereço - Informe o bairro: ")
            cidade = input("Endereço - Informe a cidade: ")
            uf = input("Endereço - Informe o estado (UF): ")

            dicionario_clientes[cpf] = {
                "nome": nome, "data_nascimento": data_nascimento,
                "rua": rua, "numero": numero, "bairro": bairro,
                "cidade": cidade, "uf": uf
                }
            print(f"Cliente: {dicionario_clientes[cpf]["nome"]} CPF: {cpf} cadastrado com sucesso!")
        
    return dicionario_clientes

# Armazenar as contas em uma lista
# Uma conta é composta por: agência, nº da conta e cliente
# O nº da conta é sequencial, iniciando em 1
# O nº da agência é fixo: "0001"
# Cada cliente pode ter mais de 1 conta
# Cada conta pode ter apenas 1 dono
def abrir_conta_corrente(dicionario_clientes, dicionario_contas, numero_da_conta):
    cpf = input("Informe o CPF do cliente: ")
    cpf = re.sub(r'\D', '', cpf)  # Remove tudo que não é número

    if cpf == "":
        print("O CPF do cliente é uma informação obrigatória!")
    else:
        # Testa se o cliente já possui cadastro
        if cpf in dicionario_clientes:
            agencia = "0001"
            numero_da_conta += 1
            saldo = 0

            dicionario_contas[cpf, agencia, numero_da_conta] = {"saldo": saldo}
            print(f"Conta: {numero_da_conta} do cliente: {cpf} aberta com sucesso!")
        else:
            print(f"O cliente: {cpf} ainda não possui cadastro!")

    return dicionario_contas, numero_da_conta


saldo = 0
extrato = ""
dicionario_clientes = {}
dicionario_contas = {}
numero_da_conta = 0
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[a] Abrir Conta Corrente
[q] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo)

    elif opcao == "s":
        saldo, extrato = saque(saldo)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        dicionario_clientes = cadastrar_cliente(dicionario_clientes)

    elif opcao == "a":
        dicionario_contas, numero_da_conta = abrir_conta_corrente(dicionario_clientes, 
                                                                  dicionario_contas, numero_da_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
