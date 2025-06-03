menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

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
            print("Depósito realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor > saldo

        limite_valor_saque = valor > limite

        limite_numero_saque = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif limite_valor_saque:
            print("Operação falhou! valor diário de saque excedeu o limite.")

        elif limite_numero_saque:
            print("Operação falhou! Atingiu número máximo diário de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n EXTRATO")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Saindo do sistema. Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
