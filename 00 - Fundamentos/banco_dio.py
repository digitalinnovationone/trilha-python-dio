## Nova versão de banco - DIO
import sys

LIMITE_DE_SAQUES = 3
valor_limite_saque = 500
saldo = 1500
transacoes = ""
numero_saques = 0


def banco():
    menu_principal= int(input( """

        [1] Saque
        [2] Deposito
        [3] Extrato
        [0] Sair

        =>"""))
    
    ##print(menu_principal)
    
    if menu_principal == 1:
        sacar()
    
    elif menu_principal == 2:
        depositar()
        outras_opcoes = int(input("Deseja realizar outro depósito? \n Escolha uma das opções abaixo: \n [1] - Sim \n [2] - Não, fazer outra operação \n: "))
        while True:
            if outras_opcoes == 1:
                depositar()
                break
                
            if outras_opcoes == 2:
                banco()
                break     
        

    elif menu_principal == 3:
        ver_extrato()
        outras_opcoes = int(input("Deseja consultar novamente o extrato? \n Escolha uma das opções abaixo: \n [1] - Sim \n [2] - Não, fazer outra operação \n: "))
        while True:
            if outras_opcoes == 1:
                ver_extrato()
                break

            if outras_opcoes == 2:
                banco()
                break
            break   
        

    elif menu_principal == 0:
        print("Você escolheu sair! Obrigado por ser cliente do Banco!")
        sys.exit()



def sacar():
    global saldo, numero_saques, transacoes
       
    valor = float(input("Digite o valor que deseja sacar: "))
    while True:
        ##exceder o saldo
        if valor > saldo:
            print("Desculpe, saldo insuficiente!")
            break
        
        ##exceder o limite
        elif valor > valor_limite_saque:
            print("O valor limite para saque é de R$500,00.")
            break
        
        ##exceder o numero de saques
        elif numero_saques >= LIMITE_DE_SAQUES:
            print("Você não pode realizar mais saques")
            banco()
            break

            
        
        
        ##realizar o saque
        elif saldo > valor:
            saldo -= valor
            transacoes += (f"Saque: R${valor:.2f}\n")
            numero_saques += 1
            outras_opcoes = int(input("Deseja realizar outro saque? \n Escolha uma das opções abaixo: \n [1] - Sim \n [2] - Não, fazer outra operação \n: "))
            while numero_saques != 3:
                if outras_opcoes == 1:
                    sacar()
                    break
                    
                else:
                    banco()
                    break

            else:
                break
        
        else:
             print("Valor informado inválido")
   

def depositar():
    global saldo, transacoes
    deposito = float(input("Digite o valor que deseja depositar: "))

    if deposito > 0:
        saldo += deposito
        transacoes += (f"Depósito: R${deposito:.2f}\n")
        print(f"O valor de R${deposito:.2f} foi depositado com sucesso")            
    
    else:
        print("Valor informado inválido")


def ver_extrato():

    print("\n--------------------------EXTRATO--------------------------")
    print("Não foram realizadas movimentações" if not transacoes else transacoes)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("-----------------------------------------------------------")
            


banco()


