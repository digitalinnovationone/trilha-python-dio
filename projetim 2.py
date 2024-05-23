

def menu():

    menu = """
        [d] - depositar
        [s] - sacar
        [e] - extrato
        [nu] - cadastrar novo usuário
        [lu] - listar usuario
        [cc] - criar conta
        [lc] - listar contas
        [q] - sair
    = 
    """
    opcao = input(menu)
    return opcao

def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            return 1
        else:
            return 0


def criar_usuario(usuarios):
    cpf = str(input("Informe o CPF (somente numero): "))
    filtro = filtrar_usuario(usuarios, cpf)

    if filtro == 1:
        print("Já existe um usuário com este cpf!")
        return

    nome = str(input("Informe o nome completo: "))
    data_nascimento = str(input("Informe a data de nascimento: "))
    endereco = str(input("Informe o endereco (logradouro, nro - bairro - cidade/sigla do estado): "))

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf,'endereco':endereco})

    print("Usuario cadastrado com sucesso!")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def depositar(saldo, valor, extrato, /): #posicional only
    
    print('Deposito')
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t valor r$ = {valor:.2f}\n"
    else:
        print("valor inválido")
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    print("Saque")
    if numero_saques < 3 and valor > 0:
        if valor <= 500:
            saldo -= valor
            numero_saques+=1
            extrato += f"Saque:\t valor = {valor:.2f}, saldo = {saldo:.2f}, numero de saques = {numero_saques}"
            print(f"Saque realizado com sucesso!, valor retirado = {valor}, saldo atual = {saldo}")
        else:
            print("Valor maximo de saque atingido, informe um valor menor que 500")
    else:
        print("Limite de saques atingido")

    return saldo, extrato, numero_saques

def Extrato(saldo, *, extrato):
    
    #extrato = f"Saldo atual = {saldo:.2f}, quantidade de saques = {numero_saques}"
    #return extrato
    print("EXTRATO")
    print("Não houve transações" if not extrato else extrato)
    print("---------------------------")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o cpf do usuário: "))

    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if usuario:
        print(f"cpf correspondente ao usuario {usuario}")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    else:
        print("Usuario não encontrado")
    
    
def listar_contas(contas):
    for conta in contas:
        print(conta)

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

        if opcao == 'd':
            
            valor = int(input("Informe o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            print(f"Valor depositado com sucesso! o saldo agora é de {saldo:.2f}")

        elif opcao == 's':
            
            valor = int(input("Informe o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 'e':
            
            extrato = Extrato(saldo, extrato=extrato)
            print(extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'lu':
            listar_usuarios(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            print("saindo...")
            break


main()