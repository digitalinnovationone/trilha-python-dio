import textwrap
def menu():
    menu = """\n
    ================ MENU ================
    [lo]\tFazer login
    [nu]\tNovo usuário
    [nc]\tNova conta

    [lu]\tLista usuário
    [lc]\tLista contas

    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
def menulogin():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato

    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /): 
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques):
    if valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print(f"\n@@@ Operação falhou! O valor do saque excede o limite de:\tR$ {limite:.2f} @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato, numero_saques
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("=== Usuário criado com sucesso! ===")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = next((usuarios[usuario] for usuario in usuarios if usuario == cpf),None)
    return usuarios_filtrados
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print("=" * 100)
        linha = f"""\
            Nome:\t{usuarios[usuario]["nome"]}
            CPF:\t{usuario}
            Endereco:\t{usuarios[usuario]["endereco"]}
            Data de nascimento:\t{usuarios[usuario]["data_nascimento"]}
        """
        print(textwrap.dedent(linha))
def criar_conta(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        limite_numero_saques = int(input("Informe o limite do número de saques diários: "))
        limite_saque = float(input("Informe o limite do valor de saque: "))
        senha = input("Informe a senha: ")
        numero_saques = 0
        saldo = 0
        extrato = ""
        numero_conta = len(contas) + 1
        contas[numero_conta] = {"agencia": agencia, "senha": senha, "usuario": usuario,
                                "limite_numero_saques": limite_numero_saques,
                                "numero_saques": numero_saques, "saldo": saldo,
                                "limite_saque": limite_saque, "extrato": extrato}
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def filtrar_contas(codigo, contas):
    contas_filtradas = next((contas[conta] for conta in contas if conta == codigo),None)
    return contas_filtradas if contas_filtradas else None
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{contas[conta]['agencia']}
            Código da conta:\t{conta}
            CPF do titular:\t{contas[conta]['usuario']}
            Limite do número de saques:\t{contas[conta]['limite_numero_saques']}
            Saques Realizados:\t{contas[conta]['numero_saques']}
            Saldo:\t{contas[conta]['saldo']}
            Limite do valor do saque:\t{contas[conta]['limite_saque']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def main():
    AGENCIA = "0001"
    ########### Abaixo alguns usuários e contas já criados
    usuarios = {'1': {'nome': 'vinícius', 'data_nascimento': '07/11/1995', 'endereco': 'lucilda minuci, 39'},
                '2': {'nome': 'exemplo', 'data_nascimento': '01/01/1990', 'endereco': 'vera cruz, 49'},
                '3': {'nome': 'exemplo2', 'data_nascimento': '01-01-1990', 'endereco': 'rua test'}}
    contas = {1: {'agencia': '0001', 'senha': '123', 'usuario': '1', 'limite_numero_saques': 2,
                  'numero_saques': 0, 'saldo': 0, 'limite_saque': 1000.0, 'extrato': ''},
              2: {'agencia': '0001', 'senha': '456', 'usuario': '2', 'limite_numero_saques': 3,
                  'numero_saques': 0, 'saldo': 0, 'limite_saque': 600.0, 'extrato': ''},
              3: {'agencia': '0001', 'senha': '789', 'usuario': '1', 'limite_numero_saques': 3,
                  'numero_saques': 0, 'saldo': 0, 'limite_saque': 500.0, 'extrato': ''}}
    while True:
        opcao = menu()
        if opcao == "lo": #Login
            codigo = int(input("Informe o código da conta: "))
            conta = filtrar_contas(codigo, contas)
            if conta:
                senha = input("Informe a senha da conta: ")
                if senha == conta['senha']:
                    while True:
                        opcao = menulogin()
                        if opcao == "d": #Depositar
                            valor = float(input("Informe o valor do depósito: "))
                            conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])
                        elif opcao == "s": #Sacar
                            if conta['numero_saques'] >= conta['limite_numero_saques']:
                                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
                                continue
                            else:
                                valor = float(input("Informe o valor do saque: "))
                                conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                                    saldo=conta['saldo'],
                                    valor=valor,
                                    extrato=conta['extrato'],
                                    limite=conta['limite_saque'],
                                    numero_saques=conta['numero_saques'])
                        elif opcao == "e": #Exibir Extrato
                            exibir_extrato(conta['saldo'], extrato=conta['extrato'])
                        elif opcao == "q": #Sair
                            break
                        else:
                            print("Operação inválida, por favor selecione novamente a operação desejada.")
                else:
                    print("\n@@@ Senha inválida, por favor selecione novamente a operação desejada. @@@")
            else:
                print("\n@@@ Conta não existe! @@@")
        elif opcao == "nu": #Criar_usuário
            criar_usuario(usuarios)
        elif opcao == "lu": #Listar_usuarios
            listar_usuarios(usuarios)
        elif opcao == "nc": #Criar_conta
            criar_conta(AGENCIA, usuarios, contas)
        elif opcao == "lc": #Listar_contas
            listar_contas(contas)
        elif opcao == "q": #Sair
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()

#Desafio: como acrescentar em usuario de usuarios os objetos contas em que o usuario é o proprietario?