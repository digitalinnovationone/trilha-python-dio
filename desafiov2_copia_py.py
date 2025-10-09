import textwrap


def menu():
    menu = """\n
    ========== MENU ========== 
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else: 
        print("\n@@@ Operaçao falhou! O valor informado e invalido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo: 
        print("\n@@@ Operaçao falhou! Voçe nao tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operaçao falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operaçao falhou! Numero maximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += "f Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== saque realizado com sucesso!")

    else:
        print("\n@@@ Operaçao falhou! O valor informado e invalido. @@@")

        return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nao foram realizadas operaçoes." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}") 
    print("=============================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero):" )
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Ja existe usuario com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data do nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("=== Usuaro criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios  if usuario ["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print("\n@@@ Usuario nao encontrado, fluxo de criaçao de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usario']['nome']}
    """
        print("= * 100")
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 1500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opçao = menu()

        if opçao == "d":
            valor  = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 
        
        elif opçao == "s":
            valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES, 
            )

        if opçao == "e":
            exibir_extrato(saldo, extrato=extrato) 
        
        elif opçao == "nu":
            criar_usuario(usuarios) 

        elif opçao == "nc":
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 

            if conta:
                contas.append(conta) 

        elif opçao == "lc":
            listar_contas(contas) 

        if opçao == "q":
            break
    
        else:
            print("Operaçao invalida, por favor selecionar novamente a oparaçao desejada. ")



        main()
