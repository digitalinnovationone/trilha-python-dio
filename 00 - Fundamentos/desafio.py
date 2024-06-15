import datetime

def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

def obter_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Operação falhou! O valor deve ser positivo.")
        except ValueError:
            print("Operação falhou! Por favor, informe um número válido.")

def depositar(saldo, extrato):
    valor = obter_valor_positivo("Informe o valor do depósito: ")
    saldo += valor
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = obter_valor_positivo("Informe o valor do saque: ")

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    print("Bem-vindo ao sistema bancário!")
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu()).strip().lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
