menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
numero_de_saques = 0
numero_de_depositos = 0
saque1 = 0
saque2 = 0
saque3 = 0
LIMITE_SAQUES = 3
LIMITE = 500


def depositar_dinheiro(valor_deposito):
    valor_deposito = float(valor_deposito)
    global saldo, numero_de_depositos
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Valor depositado com sucesso!\nSaldo em conta: R${saldo:.2f}")
        numero_de_depositos += 1
    else:
        print("Valor inválido.")
    print(saldo)
    return saldo


def sacar_dinheiro(valor_sacado):
    valor_sacado = float(valor_sacado)
    global saldo, numero_de_saques, LIMITE_SAQUES, LIMITE, saque1, saque2, saque3
    if valor_sacado <= 0:
        print("Valor inválido.")
    elif valor_sacado > LIMITE:
        print("Valor acima do limite.")
    elif numero_de_saques >= LIMITE_SAQUES:
        print("Limite de saques diarios atingido.")
    elif valor_sacado > saldo:
        print("Valor desejado é maior que o saldo em conta.")
    else:
        saldo -= valor_sacado
        print("Saque efetuado com sucesso!")
        print(f"Saldo atual da conta: R$ {saldo}")
        numero_de_saques += 1
        if numero_de_saques == 1:
            saque1 = valor_sacado
        elif numero_de_saques == 2:
            saque2 = valor_sacado
        else:
            numero_de_saques == 3
            saque3 = valor_sacado


def gerar_extrato():
    global saldo, numero_de_saques, numero_de_depositos, saque1, saque2, saque3
    print("\n================ EXTRATO ================")
    if numero_de_depositos <= 0:
        print("Não foram realizadas movimentações.")
    else:
        print(
            f"Foram realizados {numero_de_depositos} deposito(s) e {numero_de_saques} saque(s)")
        if saque1 > 0:
            print(f"Saque um: R$ {saque1:.2f}")
        if saque2 > 0:
            print(f"Saque dois: R$ {saque2:.2f}")
        if saque3 > 0:
            print(f"Saque três: R$ {saque3:.2f}")
        print(f"Saldo atual da conta: R$ {saldo:.2f}")

    print("==========================================")


while True:
    opcao = input((menu))

    if opcao == "d":
        print("Deposito")
        valor_deposito = input(
            ("Informe o valor a ser depositado: "))
        depositar_dinheiro(valor_deposito)
        print(saldo)

    elif opcao == "s":
        print("Sacar")
        valor_sacado = input(("Informe o valor a ser sacado: "))
        sacar_dinheiro(valor_sacado)

    elif opcao == "e":
        print("Extrato")
        gerar_extrato()

    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
