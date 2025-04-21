menu = """

================== MENU ==================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Insira uma opção:

==========================================

=> """

saldo = 0
limite = 500
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
            print(" ")
            print("================ SALDO =================")
            print(f"Saldo: R$ {saldo:.2f}")
            print("========================================")

        else:
            print("Operação Não Realizada! O valor informado é inválido.")

    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        saques_restantes = (LIMITE_SAQUES-numero_saques)-1

        
        if excedeu_saldo:
            print("Saldo Insuficiente Para Realizar a Operação.")

        elif excedeu_limite:
            print("O Valor do Saque Excede o Limite Contratado.")

        elif excedeu_saques:
            print("Número de Saques Diário Excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(" ")
            print("================ SALDO =================")
            print(f"Saldo: R$ {saldo:.2f}")
            print(f"Saques Restantes: {saques_restantes:.1f} ") 
            print("========================================")

        else:
            print("Operação Não Realizada! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print(" ")
        print("Obrigado por usar nossos serviços, tenha um bom dia.")

        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
