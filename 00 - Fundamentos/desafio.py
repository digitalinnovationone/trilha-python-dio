# ============== CONFIGURAÇÕES INICIAIS ==============
saldo = 0  # Variável para armazenar o saldo
limite = 500  # Limite máximo por saque
extrato = ""  # Histórico de operações
numero_saques = 0  # Contador de saques
LIMITE_SAQUES = 3  # Máximo de saques diários

# ============== FUNÇÃO PRINCIPAL ==============
while True:  # Loop infinito até o usuário sair

    # ============== MENU DE OPÇÕES ==============
    print("""
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ======================================
    """)

    opcao = input("=> ").lower().strip()  # Recebe a opção do usuário

    # ============== OPÇÃO: DEPÓSITO ==============
    if opcao == "d":
        print("\n>>> DEPÓSITO <<<")
        valor = float(input("Valor a depositar: R$ "))

        if valor > 0:  # Valida valor positivo
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n Depósito de R$ {valor:.2f} realizado!")
        else:
            print("\n Erro: Valor inválido!")

    # ============== OPÇÃO: SAQUE ==============
    elif opcao == "s":
        print("\n>>> SAQUE <<<")
        valor = float(input("Valor a sacar: R$ "))

        # Verifica regras do saque
        if valor > saldo:
            print("\n Saldo insuficiente!")
        elif valor > limite:
            print(f"\n Limite máximo por saque: R$ {limite:.2f}")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"\n Limite de {LIMITE_SAQUES} saques diários atingido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n Saque de R$ {valor:.2f} realizado!")
        else:
            print("\n Valor inválido!")

    # ============== OPÇÃO: EXTRATO ==============
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=======================================")

    # ============== OPÇÃO: SAIR ==============
    elif opcao == "q":
        print("\n Saindo do sistema... Até logo! 👋")
        break  # Encerra o loop

    # ============== OPÇÃO INVÁLIDA ==============
    else:
        print("\n⚠️ Opção inválida! Tente novamente.")

# ==================== FIM DO CÓDIGO ====================
