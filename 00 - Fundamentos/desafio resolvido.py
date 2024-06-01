saldo = 0
limite = 500
entrada = []
saida = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""
    ================ BANCO ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair        
""")
    opcao = input("=> ")

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: \n"))
        if valor > 0:
            saldo += valor
            entrada.append(valor)
            print("\nDepósito feito com SUCESSO!!\n")

        else:
            print("\nO valor informado é INVÁLIDO.\n")

    if opcao == "s":
        valor = float(input("\nInforme o valor do saque: \n"))

        if valor <= saldo and valor <= limite and valor > 0:
            numero_saques += 1

            if numero_saques > LIMITE_SAQUES:
                print("\nNúmero de saques diário ULTRAPASSADO!\n")
            else:
                saida.append(valor)
                saldo -= valor
                print("\nSaque feito com SUCESSO!\n")
            
        elif valor > saldo:
            print("\nSaldo INSUFICIENTE!\n")

        elif valor > limite:
            print("\nValor acima do LIMITE!\n")

        else:
            print("\nValor INVÁLIDO!\n")
    
    elif opcao == "e":
        print(f"""\n================ EXTRATO ================
Entradas:
    {"Não foram realizadas movimentações." if not entrada else entrada}
Saídas:
    {"Não foram realizadas movimentações." if not saida else saida}
    
Saldo: R$ {saldo:.2f}")
==========================================""")

    elif opcao == "q":
        break


        #### NAO SEI PQ APARECE QUANDO FAZ O DEPOSITO
    # else:
    #     print("\nOperação inválida, por favor selecione novamente a operação desejada.")