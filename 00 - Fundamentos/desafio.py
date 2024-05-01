menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[l] Limites
[q] Sair

=> """

saldo = 0
limite_por_saque = 500
limite_diario_saque = 1500
limite_diario_residual = limite_diario_saque

extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n  Depósito confirmado: \n   -R$ {valor:.2f}")


        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite_por_saque = valor > limite_por_saque

        excedeu_limite_diario_saque = valor > limite_diario_residual

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_por_saque:
            print("Operação falhou! O valor do saque excede o limite por saque.")

        elif excedeu_limite_diario_saque:
            print("Operação falhou! Valor diário de saques excedido.")


        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            limite_diario_residual -= valor
            numero_saques += 1
            print(f"\n  Saque autorizado: \n   -R$ {valor:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "l":
        print(f"""\n---------------- LIMITES ----------------
                  \nLimite por saque: R$ {limite_por_saque:.2f}
                  \nLimite diário para saques: R$ {limite_diario_saque:.2f}
                  \nLimite diário residual para saques: R$ {limite_diario_residual:.2f}
                  \nLimite diário de saques: {LIMITE_SAQUES}
                  \nLimite diário residual de saques: {LIMITE_SAQUES - numero_saques}
                  \n-----------------------------------------""")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
