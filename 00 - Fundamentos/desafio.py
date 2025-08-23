menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite_saque = 500
historico = ""
total_saques = 0
total_depositos = 0
valor_total_depositado = 0
valor_total_sacado = 0
LIMITE_DIARIO_SAQUES = 3

while True:
    escolha = input(menu)

    if escolha == "1":
        deposito = float(input("Valor para depósito: R$ "))

        if deposito > 0:
            saldo += deposito
            valor_total_depositado += deposito
            total_depositos += 1
            historico += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("⚠️ Valor inválido para depósito.")

    elif escolha == "2":
        saque = float(input("Valor para saque: R$ "))

        excede_saldo = saque > saldo
        excede_limite = saque > limite_saque
        excede_diario = total_saques >= LIMITE_DIARIO_SAQUES

        if excede_saldo:
            print("⚠️ Saldo insuficiente.")
        elif excede_limite:
            print("⚠️ Valor excede o limite por saque.")
        elif excede_diario:
            print("⚠️ Limite diário de saques atingido.")
        elif saque > 0:
            saldo -= saque
            valor_total_sacado += saque
            total_saques += 1
            historico += f"Saque: R$ {saque:.2f}\n"
        else:
            print("⚠️ Valor inválido para saque.")

    elif escolha == "3":
        print("\n========= EXTRATO =========")
        print(historico if historico else "Sem movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("============================")

        print("\nResumo de movimentações:")
        print(f"{'Tipo':<12}{'Qtd':<6}{'Total (R$)':>14}")
        print(f"{'-'*32}")
        print(f"{'Depósitos':<12}{total_depositos:<6}{valor_total_depositado:>14.2f}")
        print(f"{'Saques':<12}{total_saques:<6}{valor_total_sacado:>14.2f}")
        print("============================")

    elif escolha == "4":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
