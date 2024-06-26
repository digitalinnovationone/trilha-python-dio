import datetime

# Variáveis globais
saldo = 0.0
depositos = []
saques = []
saques_diarios = {}

# Função para realizar depósito
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

# Função para realizar saque
def sacar(valor):
    global saldo
    hoje = datetime.date.today()
    if valor <= 0:
        print("Valor de saque inválido.")
        return
    
    if hoje not in saques_diarios:
        saques_diarios[hoje] = 0
    
    if saques_diarios[hoje] >= 3:
        print("Limite diário de saques atingido.")
        return

    if valor > 500:
        print("O limite máximo por saque é de R$ 500,00.")
        return
    
    if valor > saldo:
        print("Saldo insuficiente.")
        return
    
    saldo -= valor
    saques.append(valor)
    saques_diarios[hoje] += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Função para visualizar extrato
def extrato():
    if not depositos and not saques:
        print("Não foram realizadas movimentações")
        return

    print("Extrato bancário:")
    print("Depósitos:")
    for deposito in depositos:
        print(f"  R$ {deposito:.2f}")
    
    print("Saques:")
    for saque in saques:
        print(f"  R$ {saque:.2f}")
    
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função principal do menu
def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor para depósito: R$ "))
            depositar(valor)
        elif opcao == '2':
            valor = float(input("Informe o valor para saque: R$ "))
            sacar(valor)
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
