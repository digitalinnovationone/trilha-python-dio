from datetime import datetime

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função que retorna a data e hora atual formatada
def datenow():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# ============================
# CADASTRO DE USUÁRIO
# ============================
def criar_usuario():
    # Solicita o CPF e verifica se já existe
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario_existente:
        print("Usuário com este CPF já existe.")
        return

    # Coleta os dados do novo usuário
    nome = input("Informe o nome completo: ").strip().title()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip().title()

    # Valida criação de senha com 8 dígitos numéricos
    while True:
        senha = input("Crie uma senha de 8 dígitos numéricos:")
        if len(senha) == 8 and senha.isdigit():
            break
        print("Senha inválida. Digite exatamente 8 números.")

    # Adiciona o usuário à lista
    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "senha": senha
    })
    print("Usuário cadastrado com sucesso!")

# ============================
# CRIAÇÃO DE CONTA CORRENTE
# ============================
def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    # Número da conta é sequencial com base no tamanho da lista de contas
    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "saques": 0
    })
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}.")

# ============================
# LISTA OS DADOS DA CONTA
# ============================
def listar_dados_conta(conta):
    print("\n=== VERIFICAÇÃO DE SEGURANÇA ===")
    senha = input("Digite sua senha para visualizar os dados da conta:")

    # Verifica se a senha informada é correta
    if conta["usuario"].get("senha") != senha:
        print("Senha incorreta. Acesso negado!")
        return
    
    usuario = conta["usuario"]
    # Exibe os dados
    print("\n=== DADOS DA CONTA ===")
    print(f"Agência: {conta['agencia']}")
    print(f"Número da conta:{conta['numero_conta']}")
    print(f"Titular: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Data de Nascimento: {usuario['nascimento']}")
    print(f"Endereço: {usuario['endereco']}")
    print("=========================")

# ============================
# DEPÓSITO
# ============================
def depositar(saldo, valor, extrato, /):  # Argumentos posicionais apenas
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} | {datenow()}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# ============================
# SAQUE
# ============================
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # Só argumentos nomeados
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} | {datenow()}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

# ============================
# EXTRATO
# ============================
def exibir_extrato(saldo, /, *, extrato):  # saldo posicional, extrato nomeado
    print("\n========= EXTRATO =========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===========================")

# ============================
# LOGIN DO USUÁRIO
# ============================
def login():
    cpf = input("CPF: ")
    contas_do_usuario = [c for c in contas if c["usuario"]["cpf"] == cpf]

    if not contas_do_usuario:
        print("Conta não encontrada.")
        return None
    
    if len(contas_do_usuario) == 1:
        conta = contas_do_usuario[0]
        print(f"\nBem-vindo(a), {conta['usuario']['nome']}! (conta {conta['numero_conta']})")
        return conta
    
    # Se tiver mais de uma conta, permite escolher
    print("\nContas encontradas para esse CPF:")
    for i, conta in enumerate(contas_do_usuario, 1):
        print(f"[{i}] Conta {conta['numero_conta']} - Agência {conta['agencia']}")
              
    while True:
        escolha = input("Digite o número da conta que deseja acessar:")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(contas_do_usuario):
                conta = contas_do_usuario[escolha - 1]
                print(f"\nBem-vindo(a), {conta['usuario']['nome']}! (Conta {conta['numero_conta']})")
                return conta
        print("Escolha inválida.")

# ============================
# MENU DE TRANSAÇÕES DA CONTA
# ============================
def menu_transacoes(conta):
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    while True:
        opcao = input("""
========= CONTA CORRENTE =========
                      
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[i] Informações da Conta

Digite a opção desejada => """)

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            conta["saldo"], conta["extrato"], conta["saques"] = sacar(
                saldo=conta["saldo"],
                valor=valor,
                extrato=conta["extrato"],
                limite=LIMITE_SAQUE_VALOR,
                numero_saques=conta["saques"],
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(conta["saldo"], extrato=conta["extrato"])

        elif opcao == "q":
            print("Encerrando sessão...")
            break

        elif opcao == "i":
            # Verificação de senha antes de mostrar dados das contas vinculadas
            print("\n=== VERIFICAÇÃO DE SEGURANÇA ===")
            senha = input("Digite sua senha para visualizar as contas vinculadas: ")

            if conta["usuario"]["senha"] != senha:
                print("Senha incorreta. Acesso negado!")
                continue

            cpf = conta["usuario"]["cpf"]
            contas_vinculadas = [c for c in contas if c["usuario"]["cpf"] == cpf]

            print(f"\n=== {len(contas_vinculadas)} CONTA(S) VINCULADA(S) AO CPF {cpf} ===")
            for c in contas_vinculadas:
                print(f"\n>>> Conta {c['numero_conta']} - Agência {c['agencia']}")
                print(f"Titular: {c['usuario']['nome']}")
                print(f"Data de Nascimento: {c['usuario']['nascimento']}")
                print(f"Endereço: {c['usuario']['endereco']}")
                print(f"Saldo: R$ {c['saldo']:.2f}")
                print("===============================")

        else:
            print("Opção inválida.")

# ============================
# PROGRAMA PRINCIPAL
# ============================
def main():
    while True:
        print("""
===== MENU PRINCIPAL =====
[1] Criar usuário
[2] Criar conta corrente
[3] Acessar conta
[0] Sair
""")
        opcao = input("Escolha uma opção => ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta_corrente()
        elif opcao == "3":
            conta = login()
            if conta:
                menu_transacoes(conta)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
