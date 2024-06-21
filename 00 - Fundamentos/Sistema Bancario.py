from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[a] Alterar Senha
[q] Sair

=> """


def formatar_extrato(extrato):
    return "\n".join([f"{transacao['data']} - {transacao['descricao']}: R$ {transacao['valor']:.2f}" for transacao in extrato])


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


nome = input("Por favor, informe seu nome: ")
senha = input("Crie uma senha para sua conta: ")
print(f"Bem-vindo ao Banco Python, {nome}!")

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato.append({"data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "descricao": "Depósito", "valor": valor})
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso, {nome}!")

            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    elif opcao == "s":
        try:
            senha_informada = input("Digite sua senha: ")
            if senha_informada != senha:
                print("Senha incorreta! Operação não autorizada.")
                continue

            valor = float(input("Informe o valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato.append({"data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "descricao": "Saque", "valor": valor})
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso, {nome}!")

            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    elif opcao == "e":
        senha_informada = input("Digite sua senha: ")
        if senha_informada != senha:
            print("Senha incorreta! Operação não autorizada.")
            continue

        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(formatar_extrato(extrato))
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "a":
        senha_informada = input("Digite sua senha atual: ")
        if senha_informada == senha:
            nova_senha = input("Digite sua nova senha: ")
            senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Senha incorreta! Operação não autorizada.")

    elif opcao == "q":
        print(f"Obrigado por usar o Banco Python, {nome}. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
