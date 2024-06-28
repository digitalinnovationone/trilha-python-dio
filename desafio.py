menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opçao = input(menu)

    if opçao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito R$ {saldo:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação Falhou! Digite um valor válido.")

    elif opçao == "s":
        saque = float(input("Qual valor você deseja sacar?: "))

        excedeu_saldo = saque > saldo

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        excedeu_limite = saque > limite

        if excedeu_saldo:
            print("Operação falhou! Sem saldo suficiente.")

        elif excedeu_limite:
            print("Limite de valor de saque por operação excedido. Tente novamente")

        elif excedeu_saque:
            print("Limite de saque diário excedido. Tente novamente amanhã!")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque relizado com sucesso!")

        else:
            print("Saque não realizado. Saldo indisponível")

    elif opçao =="e":
            print(extrato)
            print(f"Seu saldo atual é R$: {saldo:.2f}")

    elif opçao == "q":
        break

    else:
        print("opção invalida, por favor selecione novamente a opção desejada")