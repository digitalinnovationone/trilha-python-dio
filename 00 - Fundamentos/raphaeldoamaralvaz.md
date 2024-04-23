Será apresentado abaixo o código que usado nas aulas da bootcamp junto com o professor, mas abaixo, logo após a apresentação do código, estará a minha implementação do uso do código no Visual Studio Code. 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

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
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

Segue agora a minha implementação do código utilizado no Visual Studio Code:

PS C:\Users\Rafael> & C:/Users/Rafael/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Rafael/desafio.py


[d] Depositar
[s] Sacar    
[e] Extrato  
[q] Sair     

=> d
Informe o valor do depósito: 100


[d] Depositar
[s] Sacar    
[e] Extrato  
[q] Sair     

=> d
Informe o valor do depósito: 200


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 100


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 4000
Operação falhou! Você não tem saldo suficiente.


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00


Saldo: R$ 200.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 5000


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00


Saldo: R$ 5200.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 200


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00
Saque: R$ 200.00


Saldo: R$ 5000.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 600
Operação falhou! O valor do saque excede o limite.


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00
Saque: R$ 200.00


Saldo: R$ 5000.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 500


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00
Saque: R$ 200.00
Depósito: R$ 500.00


Saldo: R$ 5500.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 250


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00
Saque: R$ 200.00
Depósito: R$ 500.00
Saque: R$ 250.00


Saldo: R$ 5250.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 250
Operação falhou! Número máximo de saques excedido.


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Depósito: R$ 200.00
Saque: R$ 100.00
Depósito: R$ 5000.00
Saque: R$ 200.00
Depósito: R$ 500.00
Saque: R$ 250.00


Saldo: R$ 5250.00
==========================================


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
