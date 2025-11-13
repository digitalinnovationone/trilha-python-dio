menu = """

[d] - depositar
[s] - sacar
[e] - extrato
[q] - sair

"""

saldo = 10
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_para_depositar = float(input(print('valor para depositar: ')))
        saldo += valor_para_depositar
        print(f'depositado R$ {valor_para_depositar} e agora seu saldo é de R$ {saldo}')

    elif opcao == "s":
        LIMITES_SAQUES -= 1
        if LIMITES_SAQUES < 0:
            print("Não é possivel realizar mais saques")
            break
        valor_sacar = float(input("Digite o valor que deseja sacar "))
        if valor_sacar > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor_sacar
            print(f"Saque realizado com sucesso seu saldo agora é de R${saldo:.2f}, você tem {LIMITES_SAQUES} disponiveis ")

    elif opcao == "e":
        print(f""" 
              
            saldo: {saldo}
            limite: {limite}
            numeros de saques disponiveis: {LIMITES_SAQUES}

            """)

    elif opcao == "q":
        break

    else:
        print('Opção invalida tente novamente')
    
