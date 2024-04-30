menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Transferência
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5 

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
        print("\n--------------- EXTRATO ---------------")

        from datetime import datetime 
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Data e Hora: {data_hora}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------------------")
 

    elif opcao == "4":
        valor = float(input("Informe o valor da transferência: "))
        conta_destino = input("Informe o número da conta de destino: ")

        if valor > 0:
         if valor <= saldo: 
             saldo -= valor 
             extrato += f"Transferência para {conta_destino}: R${valor:.2f}\n"
             print("Transferência realizada com sucesso!")
         else:
             print("Operação falhou! Você não tem saldo suficiente para realizar a transferência. ")
        else:
            print("Operação falhou! Valor informado é inválido")

    

    elif opcao == "5":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
