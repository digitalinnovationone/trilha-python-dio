menu = """

[d] Depósitar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor para depósito: "))

        if valor < 0:
            print(f"R$ {valor:.2f} é inválido, por ser negativo")
        
        else:
            saldo += valor
            print(f"R$ {valor:.2f} depositado com sucesso!")

    elif opcao == "s":
        print("Saque")

        valor = float(input(f"Informe o valor de saque, saldo disponível: R$ {saldo:.2f}: "))

        if valor < 0:
            print("Valor inválido")
        elif valor > saldo:
            print(f"Você não possui limite em conta para esta operação. Saldo atual R$ {saldo:.2f} ")    
        elif valor > limite:
            print(f"O valor R$ {valor:.2f} ultrapassa o limite de R$ {limite:.2f}")
        elif numero_saques > LIMITE_SAQUES:
            print("O limite diário de saques foi atingido. Por favor tente novamente amanhã.")
        else:
            saldo -= valor
            numero_saques += 1
            print(f"O saque de R$ {valor:.2f} foi realizado com sucesso!")
        
    elif opcao == "e":
        print("Extrato")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamene a operação desejada.")