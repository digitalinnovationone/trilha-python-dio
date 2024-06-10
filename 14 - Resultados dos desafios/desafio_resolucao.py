menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
           saldo += valor
           print("\n================ EXTRATO ================")
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print(extrato)
           print(f"\nSaldo: R$ {saldo:.2f}")
           print("==========================================")
        else:
            print("Operação inválida! Informe um valor positivo para depósito")
            

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

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
            extrato = ""
            print("\n================ EXTRATO ================")
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
            numero_saques += 1

        else:
            print("Operação falhou! Informe um valor positivo para sacar.")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")