menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[l] Limite de Saques
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(valor, saldo, extrato, numero_saques):
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


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def transferir(valor, saldo, extrato):
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f"Transferência: R$ {valor:.2f}\n"
        print("Transferência realizada com sucesso!")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def mostrar_limite_saques(numero_saques, LIMITE_SAQUES):
    saques_restantes = LIMITE_SAQUES - numero_saques
    print(f"Você pode realizar mais {saques_restantes} saque(s) hoje.")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "t":
        valor = float(input("Informe o valor da transferência: "))
        saldo, extrato = transferir(valor, saldo, extrato)

    elif opcao == "l":
        mostrar_limite_saques(numero_saques, LIMITE_SAQUES)

    elif opcao == "q":
        print("Você escolheu sair! Obrigado por utilizar nosso banco.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
