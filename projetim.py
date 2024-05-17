menu = """
    [d] - depositar
    [s] - sacar
    [e] - extrato
    [q] - sair

= 
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Deposito')
        valor = int(input("Informe o valor a ser depositado: "))
        saldo += valor
        print(f"Valor depositado com sucesso! o saldo agora é de {saldo:.2f}")
    elif opcao == 's':
        print("Saque")
        numero_saques+=1
        if numero_saques < 3:
            valor = int(input("Informe o valor a ser sacado: "))
            if valor <= 500:
                saldo -= valor
                print(f"Valor sacado com sucesso! O saldo agora é de {saldo:.2f}")
            else:
                print("Valor maximo de saque atingido, informe um valor menor que 500")
        else:
            print("Limite de saques atingido")
    elif opcao == 'e':
        extrato = f"Saldo atual = {saldo:.2f}, quantidade de saques = {numero_saques}"
        print(extrato)
    elif opcao == 'q':
        print("saindo...")
        break