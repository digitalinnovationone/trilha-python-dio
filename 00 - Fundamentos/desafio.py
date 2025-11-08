LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
enderecos = {}
usuarios = {}
contas_corrente = []

def menu():
    return """

    [1] Cadastrar Usuário
    [2] Mostrar Usuários
    [3] Criar conta
    [4] Listar contas
    [5] Depositar
    [6] Sacar
    [7] Extrato
    [8] Sair

    => """

def menu_confirma_usuario():
    return """

    [n] Nome
    [d] Data de nascimento
    [c] Cpf
    [e] Endereco
    [p] Pronto

    => """

def confirma_nome_usuario():
    while True:
        nome = input("Digite o nome do usuario:")

        confirmacao = input("Tem certeza que é esse o nome?[s/n]: ").lower()

        if confirmacao == "s":
            return nome
        else:
            return "Nome não cadastrado, tente novamente."

def confirma_data_nascimento():
    while True:
        data_nascimento = input("Digite a data de nascimento do usuario [DD/MM/AAAA]: ")

        confirmacao = input("Tem certeza que é essa a sua data de nascimento?[s/n]: ").lower()

        if confirmacao == "s":
            return data_nascimento
        else:
            return "Data de nascimento não cadastrada, tente novamente"
    
def confirma_cpf_usuario():
    while True:
        cpf = input("Digite o cpf do usuario (apenas números): ").strip()

        if len(cpf) != 11 or not cpf.isdigit():
            print("Cpf deve conter exatamento 11 números. tente novamente")
            continue
        elif cpf in usuarios:
            print("Esse cpf já é cadastrado. Tente novamente.")
            continue

        confirmacao = input("Tem certeza que é esse o seu cpf?[s/n]: ").lower()

        if confirmacao == "s":
            return cpf
        else:
            return "Cpf não cadastrada, tente novamente."
    
def format_endereco(logradouro, numero, bairro, cidade_sigla, estado):
    return {
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade_sigla": cidade_sigla,
        "estado": estado
    }
    
def confirma_endereco():
    print("\n--- Cadastro de Endereço ---")
    logradouro = input("Logradouro (rua, avenida, etc.): ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade_sigla = input("Cidade/Sigla: ")
    estado = input("Estado: ")
    
    while True:
        confirmacao = input("Confirma os dados do endereço? [s/n]: ").lower()
        if confirmacao == "s":
            return format_endereco(logradouro, numero, bairro, cidade_sigla, estado)
        else:
            print("Endereço não confirmado, vamos recomeçar:")
            logradouro = input("Logradouro: ")
            numero = input("Número: ")
            bairro = input("Bairro: ")
            cidade_sigla = input("Cidade/Sigla: ")
            estado = input("Estado: ")


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    return "Usuario cadastrado com sucesso!"
    

def menu_cadastro_usuario():
    dados_usuario = {}

    while True:
        opc = input(menu_confirma_usuario()).lower()

        match opc:
            case "n":
                dados_usuario['nome'] = confirma_nome_usuario()
                print(f"Nome definido: {dados_usuario['nome']}")
            case "d":
                dados_usuario['data_nascimento'] = confirma_data_nascimento()
                print(f"Data de nascimento definido: {dados_usuario['data_nascimento']}")
            case "c":
                dados_usuario['cpf'] = confirma_cpf_usuario()
                print(f"CPF definido: {dados_usuario['cpf']}")
            case "e":
                dados_usuario['endereco'] = confirma_endereco()
                print(f"Endereco definido: {dados_usuario['endereco']}")
            case "p":
                # Verifica se todos os dados foram preenchidos
                campos_obrigatorios = ['nome', 'data_nascimento', 'cpf', 'endereco']
                if all(campo in dados_usuario for campo in campos_obrigatorios):
                    resultado = cadastrar_usuario(
                        dados_usuario['nome'],
                        dados_usuario['data_nascimento'],
                        dados_usuario['cpf'],
                        dados_usuario['endereco']
                    )
                    print(resultado)
                    break
                else:
                    print("Preencha todos os dados antes de finalizar!")
                    campos_faltantes = [campo for campo in campos_obrigatorios if campo not in dados_usuario]
                    print(f"Campos faltantes: {', '.join(campos_faltantes)}")
                    
            case _:
                print("Opção inválida! Tente novamente.")

def confirma_cpf_conta():
    while True:
        cpf = input("Digite o cpf do usuario (apenas números): ").strip()

        if len(cpf) != 11 or not cpf.isdigit():
            print("Cpf deve conter exatamento 11 números. tente novamente")
            continue
        elif cpf not in usuarios:
            print("Esse cpf não exitse. Cadastre um novo usuário ou tente novamente.")
            continue

        confirmacao = input(f"Confirma que o {usuarios[cpf]['nome']} é o titular?[s/n]: ").lower()

        if confirmacao == "s":
            return cpf
        else:
            return "Cpf não cadastrada, tente novamente."
    

def abrir_conta(agencia, numero_conta, usuarios):
    cpf = confirma_cpf_conta()  
    
    if cpf is None:
        return None  
    
    print("\nConta criada com sucesso!")
    return {
        "agencia": agencia, 
        "numero_conta": numero_conta, 
        "usuario": usuarios[cpf],
        "cpf": cpf  
    }
    

def listar_contas(contas_corrente):
    if not contas_corrente:
        print("Nenhuma conta cadastrada.")
        return
    
    for i, conta in enumerate(contas_corrente, 1):
        print(f"""
            Conta {i}:
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def extrair(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def saque(*, valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato, numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

while True:
    opc = input(menu())

    match opc:
        case "1":
            menu_cadastro_usuario()
        case "2":
            if usuarios:
                print("########-USUARIOS CADASTRADOS-########")
                for cpf, dados in usuarios.items():
                    print(f"CPF: {cpf}")
                    print(f"Nome: {dados['nome']}")
                    print(f"Data de nascimento: {dados['data_nascimento']}")
                    print(f"Endereco: {dados['endereco']['logradouro']}, {dados['endereco']['numero']} - {dados['endereco']['bairro']} - {dados['endereco']['cidade_sigla']} {dados['endereco']['estado']}")
                    print("-" * 30)
            else:
                print("Nenhum usuario encontrado.")
        case "3":
            numero_conta = len(contas_corrente) + 1
            conta = abrir_conta(AGENCIA, numero_conta, usuarios)
            contas_corrente.append(conta)
        case "4":
            if contas_corrente:
                listar_contas(contas_corrente)
            else:
                print("\nNão existem contas cadastradas.")
        case "5":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)
        case "6":    
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,)
        case "7":
            extrair(extrato, saldo)
        case "8":
            print("Saindo do sistema...")
            break
        case _:
            print("Operação inválida, por favor selecione novamente. a operação desejada.")