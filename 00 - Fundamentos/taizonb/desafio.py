"""
Dio Bootcamp Python e Vivo
Desafio de programa para implementação em sistema bancário.

Premissas: 
Não se preocupar com agência, conta corrente e senha.
            Depósito /                      Saque /                               Extrato
     apenas valores positivos       apenas valores positivos            exibir depósitos e saques.
     armazenados em 1 var.          armazenados em 1 var.               exibir saldo atual da conta
                                    apenas 3 diários.                   formato: R$ XXXX.XX
                                    limite R$500,00
                                    informar caso falte saldo

"""

#Declarando variáveis
operacoes = []
opcao = 1
saldo = 0
saques_diario = 0


#programa
while (opcao != 0):
       opcao = int(input("""
       Bem vindo ao Banco do Povo. Digite a opção desejada:

              1 - Depósito
              2 - Saque
              3 - Extrato da Conta   
              0 - Sair              
                     """))

       if (opcao == 1):
              print("""
       ========   DEPÓSITO   ========
                    """)
              #pega o valor do deposito e coloca em um dicionário
              valor = float(input("Digite o valor que gostaria de depositar: "))
              if (valor > 0):
                     operacoes.append(valor)
                     saldo += valor
                     print(f"Você depositou R$ {valor: .2f}")
                     confirmacao = input("\nPressione Enter para continuar. ")
              else:
                     print("Valor de depósito menor que zero. Favor inserir um valor positivo.")
                     confirmacao = input("\nPressione Enter para continuar. ")

       elif (opcao == 2):
              print("""
       ========     SAQUE     ========
                    """)
              #pega o valor do saque e coloca em um dicionário
              print(f"Saldo atual: R$ {saldo:.2f}\n\n")
              valor = float(input("Digite o valor que gostaria de sacar: "))
              if (valor < 0):
                     print("Favor inserir um valor positivo.")
                     continue
              elif (saldo >= valor) and (saques_diario < 3) and (valor <= 500):
                     operacoes.append(-valor)
                     print(f"Você depositou R$ {valor:.2f}")
                     saldo -= valor
                     saques_diario += 1
              elif (saques_diario >= 3):
                     print("Limite diário de saques alcançado. Limite = 3 saques.")
              elif (valor >= 500):
                     print("Valor de saque maior que o limite permitido. Limite = R$ 500,00.")
              else :
                     print("Saldo em conta insuficiente.")
                     confirmacao = input("\nPressione Enter para continuar. ")
  
       elif (opcao == 0):
              break

       elif (opcao == 3):
              print("""
       ======  EXTRATO DA CONTA  ======
                    """)
              print("   DEPÓSITOS          SAQUES")
              for num in range(len(operacoes)):
                     if (operacoes[num] > 0):
                            print(f"   R$ {operacoes[num]:.2f}")
                     else:
                            print(f"                     R$ {operacoes[num]:.2f}")
              print(f"\nSaldo Total em conta: R$ {saldo: .2f}")
              confirmacao = input("\nPressione Enter para continuar. ")

       else:
              print("Digite uma opção válida.")
              confirmacao = input("\nPressione Enter para continuar. ")


print("\nMuito obrigado. O Banco do Povo está aqui por você!")
