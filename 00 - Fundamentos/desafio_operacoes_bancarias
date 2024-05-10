saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu="""\n
----------MENU----------
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
-------------------------
Digite a opção desejada: """

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = input ("Insira o valor do depósito: R$")
        valor = int(valor)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito...: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        
    elif opcao == "s":
        if numero_saques < 3:
            valor = input("Insira o valor que deseja sacar: R$")
            valor = int(valor)
            if valor > 0 and valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque......: R$ {valor:.2f}\n"
                    print("Seu saque foi realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
        else:
            print("Você já atingiu o limite diário de saque")
    elif opcao == "e":
        print ("\n----------EXTRATO----------")
        if extrato == "":
            print("Não houve movimentações.")
        else:
            print(extrato)
        print("---------------------------")
        print(f"Seu saldo é de R$ {saldo:.2f}")
        print("---------------------------")
    elif opcao == "q":
        break
    else:
        print("Ocorreu um erro!")
