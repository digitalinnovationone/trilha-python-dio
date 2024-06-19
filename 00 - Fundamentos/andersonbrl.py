menu = """

Olá, que bom te ver por aqui!

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nSaldo: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: \n"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Saldo suficiente.")

        elif excedeu_limite:
            print("Operação inválida! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação inválida! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            print("Retire o dinheiro na boca do caixa.")
            print(f"\nSaldo: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("OBRIGADO POR SER NOSSO CLIENTE, TENHA UM BOM DIA.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
