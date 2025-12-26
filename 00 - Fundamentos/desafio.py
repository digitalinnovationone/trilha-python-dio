import textwrap

def main():
    print("Bem-vindo ao Banco Python!")
    realizar_Operacao()

def menu():
    menu = """
    ============= MENU =============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nu]\t Novo usuário
    [lu]\t Listar usuários
    [nc]\t Nova conta
    [lc]\t Listar contas
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def realizar_Operacao():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(extrato, saldo)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            visualizar_extrato(saldo, extrato)
        elif opcao == "nu":
            cadastrar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(contas, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def depositar(extrato, saldo,):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def visualizar_extrato(saldo, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    print("Cadastro de usuário")
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe o CPF: ")
    endereco = input("Informe o endereço: ")

    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado com esse CPF.")
        return ValueError("Usuário já cadastrado com esse CPF.")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print(f"Usuário {nome} cadastrado com sucesso!")

    return usuarios

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Data de Nascimento: {usuario['data_nascimento']}, Endereço: {usuario['endereco']}")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(contas, usuarios):
    print("Cadastro de conta")
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return ValueError("Usuário não encontrado. Cadastre o usuário primeiro.")

    agencia = input("Informe a agência: ")
    numero_conta = input("Informe o número da conta: ")

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, C/C: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

main()
