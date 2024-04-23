menu = """

[1] Depositar
[2] Sacar
[3] Cheque Especial
[4] Extrato
[0] Sair

=> """

saldo = 50
limite = 1500
cheque_especial = 1500
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

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo and not extrato:
            resposta = input("Você não tem saldo e não fez nenhum depósito. Deseja sacar do cheque especial? (s/n): ")
            if resposta.lower() == 's':
                if valor <= cheque_especial:
                    saldo -= valor
                    extrato += f"Saque do Cheque Especial: R$ {valor:.2f}\n"
                    numero_saques += 1
                else:
                    print("Operação falhou! O valor excede o cheque especial.")
            else:
                continue

        elif excedeu_limite:
            print("Operação falhou! O valor excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        valor = float(input("Informe o valor do cheque especial: "))

        if valor > 0 and valor <= cheque_especial:
            saldo += valor
            extrato += f"Cheque Especial: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido ou excede o cheque especial.")

    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
