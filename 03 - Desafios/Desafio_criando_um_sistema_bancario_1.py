menu = """
Bem-vindo(a) ao Banco XuaisDio!

-------------------------------

  Escolha uma opção:
  
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair
  
-------------------------------
  
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print(""" Valor inválvido!
                      Tente novamente . . . """)
    
    elif opcao == "2":
        saque = float(input("Informe o valor a ser sacado: "))

        if saque > saldo:
            print(f"Saldo insuficiente! Seu saldo atual é de R$ {saldo:.2f}\n")

        elif saque > limite:
            print(f"Você atingiu seu limite diário para saque! Volte novamente amanhã\n")

        elif saque == numero_saques >= LIMITE_SAQUES:
            print(f"Você atingiu seu limite total para saques!\n")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1 

            print(f"Saque no valor de: R$ {saque:.2f} realizado com sucesso!\n")

        else:
            print(f"Valor não reconhecido para a operação!\n")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Sem movimentações recentes" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("Obrigado por utilizar o Banco XuaisDio!")
        break

    else:
        print("Opção inválida. Confira o menu e tente novamente.\n")

        