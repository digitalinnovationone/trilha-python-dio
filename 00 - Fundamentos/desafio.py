'''
3 operações

1-depósito
    valores positivos
    armazenado em uma variável e exibidos no extrato
2-saque
    3 saques diários
    limite maximo de R$500 por saque
    caso saldo < saque "Saldo insuficiente para realizar o saque."    
    armazenado em uma variável e exibidos no extrato          
3-extrato
    listar todos depositos e saques
    no final exibir saldo atual R$xxx.xx


'''

menu = '''

Escolha uma opção:

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

'''

saldo = 30 
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:

    opcao = input(menu)

    # 1-Deposito
    if opcao == "1": 
       
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso.")
        
        else:
            print("Operação não relizada.\nValor invalido.\nO valor devo ser maior que 0.")

    # 2-Saque
    elif opcao == "2":

        # falta colocar um contador para cada saque
        if numero_saques < LIMITE_NUMERO_SAQUES:
            valor_saque = float(input("Informe o valor do saque: R$ "))

            if valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} foi realizado com sucesso.")

            else:
                print(f"Operação não realizada.\nSaldo insuficiente para realizar o saque.\nSeu saldo é de R$ {saldo:.2f}.")

        else:
            print("Operação não realizada.\nLimite de saques diários excedidos.")        


    # 3-Extrato
    elif opcao == "3": # Extrato
        print(" EXTRATO ".center(40, "="))
        print("\nNão foram realizadas movimentações no período." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(40, "="))

    # 4-Sair
    elif opcao == "4": # Sair
        break
    
    # Opção invalida
    else:
        print("Operação inválida.\nPor favor selecione a operação desejada.")

