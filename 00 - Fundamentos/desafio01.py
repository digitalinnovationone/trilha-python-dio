def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    if not any(usuario['cpf'] == cpf_numeros for usuario in usuarios):
        usuarios.append({
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf_numeros,
            'endereco': endereco
        })
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    else:
        print("CPF já cadastrado. Não é possível cadastrar o usuário.")

def criar_conta(contas, agencia, usuario):
    numero_conta = len(contas) + 1
    contas.append({
        'agencia': agencia,
        'numero_conta': f'{numero_conta:04d}',
        'usuario': usuario,
        'saldo': 0,
        'extrato': ""
    })
    print(f"Conta corrente {numero_conta:04d} vinculada ao usuário de CPF {usuario['cpf']}.")

def deposito(saldo, valor):
    saldo += valor
    return saldo

def saque(*, saldo, valor, extrato, limite=500, numero_saques=0, limite_saques=3):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

usuarios = []
contas = []
agencia = "0001"

menu = """
[c] Criar Usuário
[a] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "c":
        nome = input("Nome do usuário: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif opcao == "a":
        cpf = input("CPF do usuário para vincular à conta: ")
        usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
        if usuario:
            criar_conta(contas, agencia, usuario)
        else:
            print("Usuário não encontrado. Por favor, crie o usuário primeiro.")

    elif opcao == "d":
        numero_conta = input("Número da conta: ")
        conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                conta['saldo'] = deposito(conta['saldo'], valor)
                conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Conta não encontrada. Verifique o número da conta e tente novamente.")

    elif opcao == "s":
        numero_conta = input("Número da conta: ")
        conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta['saldo'], conta['extrato'], conta['numero_saques'] = saque(
                saldo=conta['saldo'], 
                valor=valor, 
                extrato=conta['extrato'], 
                numero_saques=conta.get('numero_saques', 0)
            )
        else:
            print("Conta não encontrada. Verifique o número da conta e tente novamente.")

    elif opcao == "e":
        numero_conta = input("Número da conta: ")
        conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
        if conta:
            extrato(conta['saldo'], extrato=conta['extrato'])
        else:
            print("Conta não encontrada. Verifique o número da conta e tente novamente.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
