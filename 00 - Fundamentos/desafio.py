import  datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques_no_dia = 0
LIMITE_SAQUES = 3
data_ultimo_saque = datetime.date.today()
print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
while True:
    print(f"Saldo atual: {saldo:.2f}")
    opcao = input(menu.lower())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques_no_dia >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            if data_ultimo_saque != datetime.date.today():
                data_ultimo_saque = datetime.date.today()
                numero_saques_no_dia = 1
            else: numero_saques_no_dia += 1
            linha = '='

            titulo = 'SAQUE'
            print("\n", titulo.center(50, '='))
            print("Saque realizado com sucesso!")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(50 * '=')
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
