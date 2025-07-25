menu = """
------------ MENU ------------

[1] Depositar
[2] Sacar
[3] Extrato
[4] Suporte para dúvidas
[0] Sair

"""

saldo = 10
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = input(menu)

    if opçao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opçao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opçao == "3":
        print("\n------------ EXTRATO ------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------------")

    elif opçao == "4":
        email = input("Informe o seu e-mail: ")
        duvida = input("Descreva a sua dúvida: ")

        if not email.endswith("@gmail.com"):
            print("E-mail inválido. Use um e-mail Google.")

        else:
            print("Agradecemos a paciência! Em breve retornaremos com uma solução.")


    elif opçao == "0":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")