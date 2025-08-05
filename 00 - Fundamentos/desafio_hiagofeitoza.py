menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
        else:
            print("⚠️ Operação falhou! Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("⚠️ Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("⚠️ Operação falhou! Valor do saque excede o limite de R$ 500.00.")
        elif excedeu_saques:
            print("⚠️ Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("⚠️ Operação falhou! Valor inválido para saque.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================\n")

    elif opcao == "q":
        print("🏦 Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("❌ Opção inválida! Selecione uma opção válida.")
