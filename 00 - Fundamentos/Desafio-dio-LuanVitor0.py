Menu_inicial = """ 
[1] - Cadastro de cliente
[2] - Lista de Cliente
[3] - Login Bancário
[4] - Sair

--> """

Lista_de_cliente = []

while True:
    opcao = input(Menu_inicial)

    if opcao == "1":
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))

        if idade >= 18:
            print(f"Cadastro realizado com sucesso.")
            Lista_de_cliente.append(nome)
        else:
            print("Cadastro exclusivo para maiores de 18 anos, conforme as normas bancárias.")

    elif opcao == "2":
        print("\n-------------------- Lista de Cadastrados -------------------------")
        if not Lista_de_cliente:
            print("Nenhum cadastrado no momento.")
        else:
            for cliente in Lista_de_cliente:
                print(f">> {cliente}")
        print("-------------------------------------------------------------------")

    elif opcao == "3":
        login = input("Digite seu nome para login: ")
        if login in Lista_de_cliente:
            print(f"Bem-vindo(a), {login}! Acesso ao sistema bancário liberado.")
            
            menu_banco = """ 
[1] - Depositar 
[2] - Sacar 
[3] - Extrato 
[0] - Sair do Banco 

--> """

            saldo = 0
            limite = 500
            extrato = ""
            numero_saque = 0
            Limite_SAQUES = 3

            while True:
                opcao_banco = input(menu_banco)

                if opcao_banco == "1":
                    valor = float(input(">> Informe o valor que deseja depositar: "))

                    if valor > 0:
                        saldo += valor
                        extrato += f"Depósito: R${valor:.2f}\n"
                        print("Depósito realizado com sucesso!")
                    else:
                        print("Valor inválido. Tente novamente.")

                elif opcao_banco == "2":
                    valor = float(input(">> Informe o valor que deseja sacar: "))

                    excedeu_saldo = valor > saldo
                    excedeu_limite = valor > limite
                    excedeu_saques = numero_saque >= Limite_SAQUES

                    if excedeu_saldo:
                        print("Saldo insuficiente.")
                    elif excedeu_limite:
                        print("Valor acima do limite por saque.")
                    elif excedeu_saques:
                        print("Número máximo de saques atingido.")
                    elif valor > 0:
                        saldo -= valor
                        extrato += f"Saque: R${valor:.2f}\n"
                        numero_saque += 1
                        print("Saque realizado com sucesso!")
                    else:
                        print("Valor inválido.")

                elif opcao_banco == "3":
                    print("\n********** EXTRATO **********")
                    print(extrato if extrato else "Nenhuma movimentação realizada.")
                    print(f"Saldo atual: R${saldo:.2f}")
                    print("*****************************")

                elif opcao_banco == "0":
                    print("Saindo do sistema bancário e voltando ao menu principal...\n")
                    break

                else:
                    print("Opção inválida no sistema bancário.")

        else:
            print("Login não encontrado. Faça o cadastro primeiro.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
