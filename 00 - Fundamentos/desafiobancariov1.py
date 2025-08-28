# Menu
menu_inicial = """

 [0] Depositar
 [1] Sacar
 [2] Extrato
 [3] Sair

==> """

# Variaveis iniciais
saldo = 0
limite_p_saque = 500
historico = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu_inicial)

    # Depositar
    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            historico += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! O valor informado é inválido.")

    # Sacar
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_p_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente para realizar esta operação.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite máximo de R$ 500,00.")

        elif excedeu_saques:
            print("A operação falhou! Número máximo de 3 saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            historico += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou! O valor informado é inválido.")

    # Extrato
    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Não há movimentações." if not historico else historico)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Sair
    elif opcao == "3":
        break

    # Opção inválida
    else:
        print("A operação falhou, por favor selecione novamente a operação desejada.")
    # Retorna ao menu novamente
