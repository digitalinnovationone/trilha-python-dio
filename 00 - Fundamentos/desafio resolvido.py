saldo = 0
limite = 500
entrada = []
saida = []
num_saques = 0
lim_saques = 3

def valor_invalido():
        print("\nO valor informado é INVÁLIDO.\n")

def depositar(valor, entrada, valor_invalido):
    global saldo
    if valor > 0:
        saldo += valor
        entrada.append(valor)
        print("\nDepósito feito com SUCESSO!!\n")
        return saldo
    else:
        valor_invalido()

def sacar(valor, limite, saida, lim_saques, valor_invalido):
    global saldo
    global num_saques
    if valor <= saldo and valor <= limite and valor > 0:
        num_saques += 1
        if num_saques > lim_saques:
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
        valor_invalido()

def extrato(entrada, saida, saldo):
    print(f"""\n\n================ EXTRATO ================
Entradas:
    {"Não foram realizadas movimentações." if not entrada else entrada}
Saídas:
    {"Não foram realizadas movimentações." if not saida else saida}
    
Saldo: R$ {saldo:.2f}
==========================================\n\n""")


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
        depositar(valor, entrada, valor_invalido)

    if opcao == "s":
        valor = float(input("\nInforme o valor do saque: \n"))
        sacar(valor, limite, saida, lim_saques, valor_invalido)  
    
    elif opcao == "e":
        extrato(entrada, saida, saldo)
        saldo = saldo

    elif opcao == "q":
        break


        #### NAO SEI PQ APARECE QUANDO FAZ O DEPOSITO
    # else:
    #     print("\nOperação inválida, por favor selecione novamente a operação desejada.")