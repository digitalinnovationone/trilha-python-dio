"""

Objetivo: Cadastrar usuário e cadastrar nova conta bancária (vinculando ao usuário). Deixar código modularizado. 
Saque: A função deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão retorno: saldo e extrato
Depósito: deve receber argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato
Extrato: deve receber os argumentos por posição e nome (positional only and keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato
Usuário: o programa deve armazenar os usuarios em uma lista: nome, data de nascimento, cpf e endereço. O endereço é uma string no formato logradouro, nro - brairro - cidade/sigla estado. Deve ser armazendado somente os numeros do CPF. Nao podemos cadastras 2 usuarios com mesmo CPF
Conta corrente: as contas devem ser armazenadas em uma lista, uma conta é composta por agência, numero da conta e usuário. O numero da conta é sequencial iniciando em 1. O numero da agencia é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

"""

import re

def menu():
    menu = """\n
    ================ MENU ================
    [d]   Depositar
    [s]   Sacar
    [e]   Extrato
    [cc]  Criar conta
    [lc]  Listar contas
    [cu]  Criar usuário
    [lu]  Listar usuário
    [q]   Sair
    => """
    operacao = input(menu)
    return operacao


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
    else:
        print("Operação falhou! O valor informado é inválido. \n")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.\n")

    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite}.\n")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.\n")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso\n")

    else:
        print(" Operação falhou! O valor informado é inválido. \n")

    return saldo, extrato


def gerar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    
    cpf = input("Informe o CPF: ")
    cpf = re.sub(r'\D', '', cpf)

    usuario = filtrar_cpf_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já está cadastrado com outro usuário! \n")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!\n")


def filtrar_cpf_usuario(cpf, usuarios):
    usuario_filtrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_filtrado = usuario
    return usuario_filtrado


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    cpf = re.sub(r'\D', '', cpf)
    usuario = filtrar_cpf_usuario(cpf, usuarios)

    if usuario:
        print(f"Conta {numero_conta} criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado! \n")


def listar_contas(contas):
    if contas:  # Verifica se a lista de contas não está vazia
        for conta in contas:
            print(f"""
            Agência:  {conta['agencia']}
            C/C:      {conta['numero_conta']}
            Titular:  {conta['usuario']['nome']}
            """)
    else:
        print("Não existem contas cadastradas.")



def listar_usuarios(usuarios):
    if usuarios:  # Verifica se a lista de contas não está vazia
        for usuario in usuarios:
            print(f"""
            Nome:  {usuario['nome']}
            CPF:  {usuario['cpf']}
            """)
    else:
        print("Não existem usuários cadastrados.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            gerar_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()