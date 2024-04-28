nome = input("Informe o seu nome: ")
print("\n")
print("Seja bem-vindo(a), " + nome + "!\n")
print("\n")
print("Escolha uma opção")

titulo = "menu"

print(titulo.center(20, "=").upper())

menu = """
[c] Cheque Especial
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

====================
\n=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print(f"Seu limite de Cheque Especial é de R$ {limite:.2f}")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"O valor de R$ {valor:.2f} foi efetuado com sucesso. Obrigado pela preferência!")
        elif valor <= saldo + limite:
            extrato += f"Saque (cheque especial): R$ {valor:.2f}\n"
            saldo -= valor
            print(f"O valor de R$ {valor:.2f} foi efetuado com sucesso. Obrigado pela preferência!")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
