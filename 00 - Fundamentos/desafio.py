#Print com as opções: sacar, depositar, extrato e sair

Menus_Sistema=
"""
=====================================

Selecione abaixo a operação desejada:

[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair

======================================
"""

#Trabalhamos com apenas um usuario nesse case e devemos:
#Depositar valores positivos na conta e todos depositos devem ser armazenados em uma variavel e exibido em extrato.
#Usuario so pode fazer 3 saques totalizando no maximo até 500 reais e caso nao tenha saldo devemos informar o usuario. Todos os saques devem ser armazenados no extrato

saldo = 1000
limite_saque = 500
op_saque = 0
limite_op_saque = 3
extrato = ""

while True:
	opção = input(menu)
	
	if opção == 1 
		valor = float(input("Qual a quantia que deseja sacar?"))
		
		excedeu_saldo  = valor > saldo
		excedeu_limite = valor > limite_saque
		excedeu_saque  = op_saque < limite_op_saque
		
		if excedeu_saldo:
			print("Opeação falhou, seu saldo é insuficiente."
		if excedeu_limite:
			print("Operação falhou, o limite de saques diarios foi atingido, tente amanhã novamente.")
		if excedeu_saque:
			print("Operação falhou, o valor limite de saque foi atingido.")
		elif valor > 0:
			saldo    -= valor
			extrato  += f"Saque: R${valor:.2f}\n"
			op_saque += 1
		else print("Opeação falho, verificar o valor informado e tente novamente")
		
	elif opção == 2
		  valor = float(input("Qual quantia deseja depositar?")) 
		  
		  if valor > 0
		  saldo  += valor
		  extrato+= f"Deposito: R${valor:.2f}\n"
		  
		  else print("Opeação falho, verificar o valor informado e tente novamente")
		  
	elif opcao == 3
			print("\n================ SEU EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
		  
	elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")	  
