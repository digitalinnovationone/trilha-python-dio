menu = """
============ Banco Py ===========
Seleciona a opção: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=================================
"""

saldo = 0
limiteSaque = 500
extrato = ""
numSaque = 0
transacoes = []
LIMITE_SAQUES = 3

def operacao(tipo, valor):
    global transacoes
    codigo = (f"{tipo}{len(transacoes) +1}", f"R$ {valor}")
    transacoes.append(codigo)
    #print(transacoes)

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Informe o valor de Depsito: R$ ").replace(',','.'))
        while deposito < 1:
            print("Deposito inválido. Insira um valor de deposito válido, acima de R$ 1.00 .")
            deposito = float(input("Informe o valor de Depsito: R$ ").replace(',','.'))
        else:
            operacao("D", deposito)
            saldo += deposito
    
    elif opcao == "s":
        print("Saque")
        if numSaque == LIMITE_SAQUES:
            print("Você atingiu o limite de saque diário.")
        
        elif saldo == 0:
            print("Você nao possue saldo suficiente para saque! Faça um deposito. :) ")
        else:
            saque = float(input("Informe o valor de Saque: R$ ").replace(',','.'))

            if saque > limiteSaque or saque < 1:
                print("O valo máximo para saque é entre R$ 1,00 a R$ 500.00.\n Tente novamente com um novo valor.")

            else:
                if saque <= saldo and saque <= limiteSaque and numSaque < LIMITE_SAQUES:
                    saldo -= saque
                    numSaque += 1
                    operacao("S", saque)
                else:
                    print("Operação inválida... Consulte saldo disponível para saque!")

    elif opcao == "e":
        print("Extrato")
        for dados in transacoes: print(dados, sep="\n")
        print(f"\nSaldo Atual: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


