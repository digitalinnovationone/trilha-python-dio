def depositar(saldo, extrato):
    valor = float(input("Informe o valor a ser depositado: "))

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print("Depósito realizado!")
    
    else:
        print("Valor invalido! Informe um valor positivo.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    valor = float(input("Informe um valor para saque: "))

    if valor<= 0:
        print("Valor invalido!")

    elif valor > saldo:
        print("Saldo insuficiente.")

    elif valor > limite:
        print(f"Limite de saque é de R${limite:.2f}")

    elif numero_saques >= limite_saques:
        print("Numero maximo de saques atingido")

    else:
        saldo -= valor
        extrato.append(f"Saque:  R${valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================\n")


def main():
    saldo = 0.0
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()