menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """  # Menu de opções para o usuário

saldo = 0  # Inicializa o saldo da conta como 0
limite = 30000  # Define o limite máximo de saque
extrato = ""  # Inicializa o extrato vazio
numero_saques = 0  # Inicializa o contador de saques
LIMITE_SAQUES = 5  # Define o limite de saques diários

while True:  # Loop principal do programa

    opcao = input(menu)  # Exibe o menu e recebe a opção do usuário

    if opcao == "1":  # Opção de depósito
        
        try:  # Tenta executar o bloco de código
            valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
            
            if valor > 0:  # Verifica se o valor é válido
                saldo += valor  # Adiciona o valor ao saldo
                extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona a transação ao extrato
                print("Depósito realizado com sucesso!")  # Mensagem de sucesso
            
            else:
                print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro
        
        except ValueError:  # Captura erros de valor inválido
            print("Valor inválido. Digite um número.")  # Mensagem de erro

    elif opcao == "2":  # Opção de saque
       
        try:  # Tenta executar o bloco de código
            valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque

            excedeu_saldo = valor > saldo  # Verifica se o saque excede o saldo
            excedeu_limite = valor > limite  # Verifica se o saque excede o limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se excedeu o limite de saques

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")  # Mensagem de erro
            
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")  # Mensagem de erro
            
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")  # Mensagem de erro
            
            elif valor > 0:  # Verifica se o valor é válido
                saldo -= valor  # Subtrai o valor do saldo
                extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona a transação ao extrato
                numero_saques += 1  # Incrementa o contador de saques
                print("Saque realizado com sucesso!")  # Mensagem de sucesso
            
            else:
                print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro
        
        except ValueError:  # Captura erros de valor inválido
            print("Valor inválido. Digite um número.")  # Mensagem de erro

    elif opcao == "3":  # Opção de extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)  # Exibe o extrato ou mensagem
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("==========================================")

    elif opcao == "4":  # Opção de sair
        
        break  # Encerra o loop principal

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro
