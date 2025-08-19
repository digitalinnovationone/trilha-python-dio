import textwrap




def menu():
    
    
    menu = """
    ==========Banco do Daniel===========

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Cliente
    [cc] Cadastrar Conta Bancária
    [l] Listar Clientes
    [lc] Listar Contas Bancárias
    [q] Sair

    ====================================
    

    => """
    escolha =  input(textwrap.dedent(menu).strip())
    return escolha.lower()

def cadastrar_cliente(clientes: list):

    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do cliente (apenas números): ").replace(".", "").replace("-", "")
    
    if any(cliente['cpf'] == cpf for cliente in clientes):
        print("CPF já cadastrado. Tente novamente.")
        return
    
    endereco = input("Digite o endereço do cliente (Logradouro, número - Bairro - Cidade/UF): ")

    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print(f"Cliente {nome} cadastrado com sucesso!")

def cadastrar_conta(clientes: list, contas: list):
    agencia = "0001"
    numero_conta = len(contas) + 1 
    cpf = input("Digite o CPF do cliente para vincular a conta: ").replace(".", "").replace("-", "")
    if not any(cliente['cpf'] == cpf for cliente in clientes):
        print("CPF não cadastrado. Por favor, cadastre o cliente primeiro.")
        return
    cliente = next(cliente for cliente in clientes if cliente['cpf'] == cpf)
    contas.append({
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cliente': cliente
    })
    print(f"Conta {numero_conta} cadastrada com sucesso para o cliente {cliente['nome']}!")

def listar_clientes(clientes: list):

    if not clientes:
        print("Erro: Nenhum cliente cadastrado.")
        return
    print("\nLista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}")

def listar_contas(contas: list):

    if not contas:
        print("Erro: Nenhuma conta bancária cadastrada.")
        return
    print("\nLista de Contas Bancárias:")
    for conta in contas:
        cliente = conta['cliente']
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Cliente: {cliente['nome']}, CPF: {cliente['cpf']}")

def deposito( saldo: float, extrato_cliente: str, /):
        valor_a_depositar = float(input("Digite o valor que deseja depositar"))
        
        if valor_a_depositar >= 0.01:

            saldo += valor_a_depositar
            print(f"Saldo atual é de R${saldo:.2f}.")
            extrato_cliente += f"depósito de R${valor_a_depositar:.2f}.\n"
            return saldo, extrato_cliente
        else:
            print("Valor Inválido para Depósito")

def saque(*, saldo: float, extrato_cliente:  str, limite: int, numero_saques: int, limite_saques: int):
        valor_a_sacar = float(input("Digite o valor que deseja sacar."))
        

        if valor_a_sacar > saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
            pass
        elif valor_a_sacar > limite:
            print('Operação falhou! O valor do saque excede o limite.')
            pass

        elif numero_saques >= limite_saques:
            print('Operação falhou! Número máximo de saques excedido.')
            pass
                    
        else:
            saldo = saldo - valor_a_sacar
            extrato_cliente += f"Saque de R${valor_a_sacar:.2f}.\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual é de R${saldo:.2f}.")
            return saldo, extrato_cliente, numero_saques

def extrato( saldo, *, extrato_cliente): 
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato_cliente)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    escolha = ""
    saldo = 0
    limite = 500
    extrato_cliente = ""
    numero_saques = 0
    limite_saques = 3
    clientes = []
    contas = []
    
    while escolha != "q" and escolha != "Q":

        escolha = menu()
        
        if escolha == "s":
            try:

                saldo, extrato_cliente, numero_saques = saque( saldo=saldo, extrato_cliente=extrato_cliente, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
                print(f"Saldo atual é de R${saldo:.2f}.")
                
            except TypeError:
                print("Voltando ao menu principal, por favor tente novamente.")    

        elif escolha == "d":
            saldo, extrato_cliente = deposito(saldo, extrato_cliente)

        elif escolha == "c":    
            cadastrar_cliente(clientes)

        elif escolha == "cc":  
            cadastrar_conta(clientes, contas)

        elif escolha == "l":
            listar_clientes(clientes)

        elif escolha == "lc":
            listar_contas(contas)
              
        elif escolha == "e":
            extrato(saldo, extrato_cliente=extrato_cliente)       

        elif escolha =="q": 
            print('Encerrando a operação')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
           
       
              
if __name__ == "__main__":
    main()
