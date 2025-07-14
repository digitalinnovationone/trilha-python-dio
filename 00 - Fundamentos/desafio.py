menu = """
[d] Depositar
[w] Sacar
[s] Extrato
[p] Pix
[e] Sair

=> """

saldo = 0
limite_saque = 2000
limite_pix_diario = 2000
extrato = ""
numero_saques = 0
valor_pix_utilizado = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! Informe um valor positivo para depósito.")

    elif opcao == "w":
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Valor inválido! Informe um valor positivo para saque.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite_saque:
            print(f"Operação falhou! Limite por saque é de R$ {limite_saque:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "p":
        chave = input("Digite a chave Pix (email, CPF ou telefone): ").strip()
        valor = float(input("Informe o valor do Pix: "))

        if valor <= 0:
            print("Valor inválido! Informe um valor positivo para Pix.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente para Pix.")
        elif valor_pix_utilizado + valor > limite_pix_diario:
            print("Operação falhou! Limite diário de Pix excedido.")
        else:
            saldo -= valor
            valor_pix_utilizado += valor
            extrato += f"Pix enviado para {chave}: R$ {valor:.2f}\n"
            print(f"Pix de R$ {valor:.2f} enviado para {chave} com sucesso.")

    elif opcao == "s":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Saques realizados hoje: {numero_saques}/{LIMITE_SAQUES}")
        print(f"Pix utilizado hoje: R$ {valor_pix_utilizado:.2f} de R$ {limite_pix_diario:.2f}")
        print("================================")

    elif opcao == "e":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida, por favor selecione novamente.")
