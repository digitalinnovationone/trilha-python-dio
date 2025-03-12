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

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Digite o valor do deposito: "))
        if valor >= 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operacao Invalida. Digite novamente o valor.")
    

    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo Insuficiente!")

        elif valor > limite:
            print("Limite de saque excedido")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operacao Invalida. Numero de saques excedido")

        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao Invalida. Digite novamente o valor.")

    elif opcao == "e":
        print("\n=============Extrato===============")
        print("Nao foram realziadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:2f}")
        print("=====================================")


    elif opcao == "q":
        break

    else: 
        print("Operacao Invalida")