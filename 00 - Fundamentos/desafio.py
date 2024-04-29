menu = """
            MENU
[1] Depositar   [2] Sacar
[3] Extrato     [4] Sair

=> """

NUMERO_LIMITE_SAQUES = 3
VALOR_LIMITE_SAQUE = 500

saldo = 0
extrato = ""
numero_saques = 0


while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        #Permite apenas valores positivo de depósito
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
        else:
            print("Valor inválido, não foi possível realizar depósito.")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        #O sistema só deve permitir 3 saques diários
        if numero_saques >= NUMERO_LIMITE_SAQUES:
            print("Operação falhou! Número de saques diário foi excedido.")
        #O valor máximo de saque é R$ 500,00
        elif valor > VALOR_LIMITE_SAQUE:
            print(f"Operação falhou! O valor do saque excede R$ {VALOR_LIMITE_SAQUE:.2f}.")
        #Verifica saldo insuficiente
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "3":
        print("EXTRATO".center(41,"="))
        #if ternário 
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(41*"=")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")