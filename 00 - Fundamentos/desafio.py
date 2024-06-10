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
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Valor: "))
        saldo += valor
        extrato += f"Deposito de R$ {valor}\n"
        print("Deposito realizado com sucesso!")
        print(f"Novo saldo: R$ {saldo}")
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
        valor = float(input("Valor: R$"))
        if valor > saldo:
            print("Saldo insuficiente")
        if valor > 500:
            print("Valor não permitido.")
        
        else:
            saldo -= valor
            extrato += f"Saque de R${valor}\n"
            print("Saque realizado com sucesso!")
            print(f"Novo saldo: {saldo}")
            numero_saques += 1
            print(f"Numero de saques: {numero_saques}")

    elif opcao == 'e':
        if saldo > 0:
            print(extrato)
            print("Seu saldo é de: R$",saldo)
        else: 
            print("Não houve movimentações")
    elif opcao == 'q':
        break
    else:
        print("Opção inválida")




