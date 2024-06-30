# Trilha Python DIO

import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_DEPOSITO = 5000  # New limit
LIMITE_SAQUE = 500  # New limit

def depositar(valor):
    global saldo, extrato
    if 0 < valor <= LIMITE_DEPOSITO:
        saldo += valor
        extrato.append((datetime.datetime.now(), "Depósito", valor))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Seu novo saldo é R$ {saldo:.2f}")
    else:
        print(f"Operação falhou! O valor deve estar entre R$ 0.01 e R$ {LIMITE_DEPOSITO:.2f}.")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_SAQUE  # Using new limit
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f}.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif 0 < valor <= saldo:
        saldo -= valor
        extrato.append((datetime.datetime.now(), "Saque", valor))
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Seu novo saldo é R$ {saldo:.2f}")
    else:
        print(f"Operação falhou! O valor deve estar entre R$ 0.01 e R$ {saldo:.2f}.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for data, operacao, valor in extrato:
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {operacao}: R$ {valor:.2f}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():  # Main function to encapsulate the logic
    while True:
        opcao = input(menu)
        # ... (rest of the code is the same as before)

if __name__ == "__main__":
    main()
