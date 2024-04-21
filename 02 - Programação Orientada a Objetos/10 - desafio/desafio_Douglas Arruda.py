CONTA_USUARIO = True
LIMITE_SAQUES = 3

saldo = 1000.45
limite = 500
extrato = ""
numero_saques = 0
menu = '''
================ MENU ================

(1) DEPOSITAR
(2) SACAR
(3) EXTRATO
(4) SAIR

======================================
=> '''

while True:

    opcao = input(menu)
    
    if opcao == "1":
        print("\n================ Deposito ================")
        valor = float(input("Informe o deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print("==========================================")

        else:
            print("Operação falhou! O valor é inválido.")

    elif opcao == "2":
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        print("==========================================")

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if  not extrato else extrato)
        print("==========================================")

    elif opcao == "4":
        print("Obrigado por acessar nosso Banco, Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    
