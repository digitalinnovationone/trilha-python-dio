import locale
import time

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

menu = """
Selecione a opção desejada:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Informe a opção =>
"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
numero_de_depositos = 0
LIMITE_DEPOSITOS = 3


def exibir_extrato(saldo, extrato):
    print("=== EXTRATO ===")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: {locale.currency(saldo, grouping=True)}")
    print("=================")
    time.sleep(1)


def deposito(saldo, extrato, valor):
    global numero_de_depositos
    excedeu_valor_limite = valor > limite
    excedeu_numero_depositos = numero_de_depositos >= LIMITE_DEPOSITOS

    if excedeu_numero_depositos:
        print("Limite de depósitos atingido.")
    elif valor <= 0:
        print("Valor inválido para depósito.")
    elif excedeu_valor_limite:
        print("Valor acima do limite permitido para depósito.")
    else:
        saldo += valor
        extrato += f"Depósito: {locale.currency(valor, grouping=True)}\n"
        numero_de_depositos += 1
        print(f"Depósito de {locale.currency(valor, grouping=True)} realizado com sucesso!")

    return saldo, extrato

time.sleep(1)


def saque(saldo, extrato):
    global numero_de_saques
    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
    valor = float(input("Informe o valor a ser sacado: R$ "))

    if excedeu_saques:
        print("Número máximo de saques atingido.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    elif valor > limite:
        print("Valor acima do limite permitido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato += f"Saque: {locale.currency(valor, grouping=True)}\n"
        numero_de_saques += 1
        print(f"Saque de {locale.currency(valor, grouping=True)} realizado com sucesso!")

    return saldo, extrato

time.sleep(1)


while True:
    print("Bem-vindo ao banco DIO!")
    opcao = input(menu)
    time.sleep(1)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: R$ "))
        saldo, extrato = deposito(saldo, extrato,valor)
    elif opcao == "2":
        saldo, extrato = saque(saldo, extrato)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "0":
        print("\nEncerrando sessão...")
        time.sleep(1)
        print(f"\nResumo da sua conta:")
        print(f"Depósitos realizados: {numero_de_depositos}/{LIMITE_DEPOSITOS}")
        print(f"Saques realizados: {numero_de_saques}/{LIMITE_DE_SAQUES}")
        print(f"Saldo final: {locale.currency(saldo, grouping=True)}")
        print("\n Obrigado por utilizar o banco DIO! Volte sempre. 😊")
        break
    else:
        print("Opção inválida. Tente novamente.")


