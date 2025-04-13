# Configurações iniciais
saldo = 0.0
limite_por_saque = 1000.0
extrato = []
quantidade_saques = 0
LIMITE_SAQUES_DIARIO = 3

# Menu principal
while True:
    print("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    """)
    
    opcao = input("Escolha uma opção: ")
    
    # Opção de Depósito
    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")
    
    # Opção de Saque
    elif opcao == "2":
        if quantidade_saques >= LIMITE_SAQUES_DIARIO:
            print("Limite diário de saques atingido!")
            continue
            
        valor = float(input("Digite o valor para saque: "))
        
        if valor <= 0:
            print("Valor inválido para saque!")
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite_por_saque:
            print(f"Valor excede o limite de R$ {limite_por_saque:.2f} por saque")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            quantidade_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    # Opção de Extrato
    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        if not extrato:
            print("Não houve movimentações")
        else:
            for movimento in extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("======================================")
    
    # Opção de Sair
    elif opcao == "4":
        print("Encerrando o sistema...")
        break
    
    # Opção inválida
    else:
        print("Opção inválida! Tente novamente.")