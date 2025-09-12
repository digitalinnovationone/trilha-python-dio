def menu():
    menu = """\n
    =========== MENU ===========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [0] Sair

    ============================
    """ 
    return(input(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente. ")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite. ")

    elif excedeu_saques: 
        print("Operação falhou! Limite de saques excedido. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        
        return saldo, extrato

def depositar(saldo, valor, extrato, /):


    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n========== EXTRATO  ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: (dd/mm/aaaa)")
    endereco = input("Informe o endereço (logradouro - nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
   
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_contas": numero_contas, "usuarios": usuarios}
    
    print("Usuário não encontrado!")

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
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "0":
            break

        else:
            print("Operação Inválida! Por favor, selecione a opção desejada.")

main()




            
    

    




    




 



