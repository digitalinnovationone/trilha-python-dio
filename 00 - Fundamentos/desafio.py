menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato):
    if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def gerar_extrato(extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(saldo, valor, extrato)

    elif opcao == "e":
        gerar_extrato(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
