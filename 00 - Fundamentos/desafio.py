menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000.0
limite = 500.0
extrato = "\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    
    if opcao == "d":
        valor_deposito = float(input("Qual o valor você deseja depositar? "))
        if valor_deposito <= 0:
            print(f"Valor não pode ser menor do que 0")
            
        else:
            extrato += f"Deposito: R${valor_deposito:.2f}\n" 
            saldo += valor_deposito
            print(f"R${valor_deposito} depositado! Seu novo saldo é R${saldo}")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

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
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n======================= EXTRATO =======================")
        print(f""" Saldo atual R$ {saldo} 
            {extrato}""")
        print("=======================================================")
    elif opcao == "q":
        break
    else:
        print("Operação não valida")