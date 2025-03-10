
menu = """Bem vindo ao Banco

[1] - Depositar
[2] - Saque
[3] - extrato
[0] - Sair """

opcao = -1
saldo = 0
limite = 500
Historico_extrato = []
Numero_saques = 0
Limite_saques = 3


def deposito(valor):
    global saldo, Historico_extrato
    if deposito > 0:
        saldo += valor
        Historico_extrato.append(f'deposito de R$ {valor:.2f}')
        print("Deposito efetuado")
    else:
        print("Valor inválido")

def sacar(valor):
    global saldo, Historico_extrato, Numero_saques
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Limite de saque excedido") 
    elif Numero_saques >= Limite_saques:
        print("Limite de saques diários excedido")
    elif valor > 0:
        saldo -= valor
        Numero_saques +=1
        Historico_extrato.append(f"saque de R$ {valor:.2f}")
    else:
        print("Valor inválido")
    

def extrato():
    global saldo, Historico_extrato
    if len(Historico_extrato) == 0:
        print("Nenhuma transação realizada")
    else:
        for item in Historico_extrato:
            print(item)
    print(f"Saldo: R$ {saldo:.2f}")
    

while opcao != 0:

    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input("Digite o valor do deposito:"))
        deposito(valor)
    elif opcao == 2:
        valor = float(input(" digite o valor do saque: "))
        sacar(valor)
    elif opcao == 3:
        extrato()
    elif opcao == 0:
        print("Volte sempre")
    else:
        print("Opção inválida")
