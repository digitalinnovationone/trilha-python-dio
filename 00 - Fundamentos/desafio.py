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


## loop principal
while 1 == 1:
    '''armazena a opção do usuário'''
    opcao = input(menu)

    ## opção [d] - DEPÓSITO
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("FALHA NA OPERAÇÃO! O valor informado é inválido")

    ## opção [s] - SAQUE
    elif opcao == "s":
        ''' 1ª verificação - limite de saques (3) '''
        if numero_saques >= LIMITE_SAQUES:
            print("FALHA NA OPERAÇÃO! O número máximo de saques excedido.")

        else:
            valor = float(input("Informe o valor para saque: "))
        
            ''' 2ª verificação - saldo suficiente '''
            excedeu_saldo = valor > saldo
            ''' 3ª verificação - valor limite do saque (R$500,00) '''
            excedeu_limite = valor > limite

            if excedeu_saldo:
                print("FALHA NA OPERAÇÃO! Você não tem saldo suficiente")

            elif excedeu_limite:
                print("FALHA NA OPERAÇÃO! O valor do saque exece o limite")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("FALHA NA OPERAÇÃO! O valor informado é inválido")

    ## opção [e] - EXTRATO
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    ## opção [q] - SAIR
    elif opcao == "q":
        break

    else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")