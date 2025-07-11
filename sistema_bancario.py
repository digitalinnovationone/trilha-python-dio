print("\nSeja Bem-Vindo ao sistema bancário DIO by Tiago-Pereira-devv")

erro_opcao = f""" 
       **SELECIONE UMA OPÇÃO VÁLIDA!**
"""
menu = f"""
------------SELECIONE UMA OPÇÃO-------------
[1] DEPOSITAR [2] SACAR [3] EXTRATO [0] SAIR
-> """

extrato = ""

saldo = 0

limite = 500

limite_saque = 3

numero_saque = 0

while True: #inicia laço após apresentação do menu
    
    opcao = input(menu)
    
    if opcao == "1": #solicita valor para depósito, evita que seja inserido um valor menor ou igual a 0, deposita valor e atribui a saldo, operação ok salva info na var "extrato"
        deposito = float(input(("Informe o valor do depósito\nR$: ")))

        if deposito > 0:
            saldo += deposito
            print(f"\nDepósito no valor de: R${deposito: .2f} efetuado com sucesso!")
            extrato += f"|ENTRADA| no valor de: R${deposito:>9.2f}\n"
        else:
              print("\nFALHA NA OPERAÇÃO. DIGITE UM VALOR VÁLIDO PARA DEPÓSITO!")
              
                          
    elif opcao == "2":   #Permite 3 saques diários com limite maximo de 500,00 por saque, se saque for maior que saldo ou saque for igual a zero gera erro. 
        
        saque = float(input("Informe o valor do Saque:\nR$ "))   
        
        excedeu_saque = numero_saque >= limite_saque
        
        excedeu_saldo = saque > saldo
        
        excedeu_limite = saque > limite
               
        if excedeu_saldo:
            print("...FALHA NA OPERAÇÃO. CONTA SEM SALDO, VERIFIQUE O SEU EXTRATO")
            
        elif excedeu_limite:
            print(f"...FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA SAQUE INDIVIDUAL MAIOR QUE R$:{limite: .2f}")
        
        elif excedeu_saque:
            print(f"...FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA MAIS DE 3 SAQUES POR DIA")
        
        elif saque > 0:
            numero_saque += 1  
            extrato += f"|SAÍDA| no valor de: R${saque:>11.2f}\n"  
            saldo -= saque
            print(f"Saque de R${saque: .2f} feito com sucesso!") 
        else:
            print("...FALHA NA OPERAÇÃO. INSIRA UM SALDO VÁLIDO PARA SAQUE")
            
    elif opcao == "3": #imprime extrato. Se extrato tiver vazio retorna mensagem. String concatenada para visual agradável no terminal
        print("============= EXTRATO =============")
        print(f"{extrato if extrato else 'Nenhuma movimentação realizada.'}")
        print(f" SALDO ATUAL: R${saldo: .2f}")
        print("===================================")
    
    elif opcao == "0": #encerra o programa com quebra do laço
        print("...PROGRAMA ENCERRADO PELO USUÁRIO")
        break
    
    else: #retorna erro caso opção do usuário seja diferente de 1,2,3 ou 0.
        print(erro_opcao)  