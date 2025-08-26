# menu incial
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
# iteração do sistema
while True:

    opcao = input(menu)
# op deposito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
# deposito deve ser um valor acima de 0
        if valor > 0:
            saldo+=valor
            extrato+=(f"Depósito: + R$ {valor:.2f}\n")
            print("Operação válida, epósito realizado com sucesso!")
        else:
            print("Operação inválido, depósito não realizado.")
# op saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
# saque deve ser até 500 reais, menor ou igual ao saldo e tem limite de 3 vezes diárias
        valor_max_saque = 0 < valor <= 500
        saque_menor_saldo = valor <= saldo
        quantidade_saques = LIMITE_SAQUES >= numero_saques    
# se o saque for qualificável
        if valor_max_saque and saque_menor_saldo and quantidade_saques is True:
            saldo-=valor
            numero_saques+=1
            extrato+=(f"Saque: - R$ {valor:.2f}\n")
            print("Operação válida, saque realizado com sucesso!")
# por que o saque não é qualificável
        elif valor_max_saque is False:
            print("Operação inválida, saque permitido de até R$500.00.")
        elif saque_menor_saldo is False:
            print("Operação inválida, saldo insuficiente.")
        elif quantidade_saques is False:
            print("Operação inválida, limite diário de saques já foi atingido.")
# op extrato
    elif opcao == "e":
        print("EXTRATO".center(27,"="))
        print(f"Sua atividade na conta:\n{extrato}")
        print(f"Seu saldo atual: R$ {saldo:.2f}")
        print("".center(27,"="))
# op de sair
    elif opcao == "q":
        break
# se nenhuma op for selecionada/escrita errada
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
