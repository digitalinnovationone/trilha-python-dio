#menu das opções que serão exibidas para o usuário tnteragir
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0 #No nosso caso saldo sempre inicia com zero
limite = 500 #Limite de retirada por operação
extrato = "" #string iteravel que inicia vazia, serve depois para nossa condicional no extrato.
numero_saques = 0 #Contador começa em 0
LIMITE_SAQUES = 3

while True: #Enquanto tudo for verdade executa:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: \n"))

        if valor > 0:                                                   #Se o depósto é num valor maior que zero o saldo é incrementado e o extrato exibido
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" #Retorna só até 2 casas decimais ex 1.99

        else:
            print("Operação falhou! A quantia informada não é válida.\n")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: \n"))

        excedeu_saldo = valor > saldo       #atribuindo nova variável apara condições mais a frente: O valor de saque excede o que tem na conta

        excedeu_limite = valor > limite #o valor de saque maior que o limite de 500 reais por solicitação

        excedeu_saques = numero_saques >= LIMITE_SAQUES # o numero de saques se limita a 3 solicitações por dia.

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.\n")

        elif excedeu_saques:
            print("Operação falhou! Limite de saques excedidos.\n")

        elif valor > 0:                         #Caso não tenha excedido nada... Esta linha de código vem depois pois primero verificamos se não há nenhuma restraição para liberar $$
            saldo -= valor                      # o valor solicitado vai decrementar o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 #o Contador de saque vai aumentar em 1 a cada iteração

        else:
            print("Operação falhou! A quantia informada não é válida.\n") # por exemplo se estiver com a conta zerada...

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:  #como no inicio declaramos que tudo era True no While, aqui é uma opção que se for False vire True para não sair do programa
            print("Não foram realizadas movimentações.\n")
        else:
            print(extrato) #exibe as movimentações registradas e seus valores
        
        print(f"\nSaldo: R$ {saldo:.2f}\n")     #Se colocar dentro da condição só mostra o saldo quando ouver movimentação mas no geral nos dá o saldo na conta
        print("==========================================")

    elif opcao == "4":
        print("Obrigada por ser nosso cliente. Tenha um ótimo dia!\n")
        break

    else: # se digitar opção que não as enumeradas

        print("Operação inválida, por favor selecione novamente a operação desejada.\n") 
