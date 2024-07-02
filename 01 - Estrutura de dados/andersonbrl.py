
def menu():
    menu = """\n
    
    Olá, que bom te ver por aqui!\n
    ============ MENU ============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar conta
    [7]\tSair
    => """
    return input(menu)
    

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:R$ {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso!===")
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    else:
        print("\n*** Operação falhou! Ovalor informado é inválido. ***")
        
    return saldo, extrato      

def sacar(*,saldo,valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\nSaldo insuficiente. ")
    
    elif excedeu_limite:
        print("O valor do saque excede o limite.  ")
        
    elif excedeu_saques:
        print("Número máximo de saques excedido. ")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    
    else:
        print("\nO valor informado é inválido. ")
        
        return saldo, extrato       
    
    
    def exibir_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
  
def exibir_extrato(saldo, /, *, extrato):
    print("\n============= EXTRATO ============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("====================================")
               
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")   
    usuarios = filtrar_usuario(cpf, usuarios)
    
    if usuarios:
        print("Já existe usuario com esse cpf! ")
        return
    
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro,número - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nacimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso! ")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    
         
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuarios:
        print("\n=== Conta criada com sucesso ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("**** Usúario não encotrado. ")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(linha)                          

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
    
        if opcao == "1":
           valor = float(input("Informe o valor do depósito: "))
        
           saldo, extrato = depositar(saldo,valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
        
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuario("usuarios")
        
        elif opcao == "5":
            numero_conta = len(conta) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
             contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == "7":
            print("OBRIGADO POR SER NOSSO CLIENTE, TENHA UM BOM DIA.")
            break
    
        else:
            print("Operação invalida, por favor selecione a operação desejada. ")

main()  
