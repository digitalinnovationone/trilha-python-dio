menu = """
Banco do Daniel

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
   
    escolha = input(menu)

    if escolha == "d":
        valor_a_depositar = float(input("Digite o valor que deseja depositar"))
        
        if valor_a_depositar >= 0.01:

            saldo += valor_a_depositar
            print(f"Saldo atual é de R${saldo:.2f}.")
            extrato += f"depósito de R${valor_a_depositar:.2f}.\n"
        else:
            print("Valor Inválido para Depósito")

    elif escolha == "s":
        valor_a_sacar = float(input("Digite o valor que deseja sacar."))
        

        if valor_a_sacar > saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif valor_a_sacar > limite:
            print('Operação falhou! O valor do saque excede o limite.')

        elif numero_saques >= limite_saques:
            print('Operação falhou! Número máximo de saques excedido.')
                    
        else:
            saldo = saldo - valor_a_sacar
            extrato += f"Saque de R${valor_a_sacar:.2f}.\n"
            numero_saques += 1

    elif escolha == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif escolha =="q": 
        print('Encerrando a operação')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
              
