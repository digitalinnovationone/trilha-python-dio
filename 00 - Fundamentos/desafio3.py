def exibir_menu():
    print("""
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastro usuario
[c] Cadastro conta bancária
[l] Listar contas
[q] Sair
""")

def depositar (saldo, valor, extrato, /):

    if valor > 0:
       saldo += valor
       extrato += f"deposito R$ {valor:.2f}\n"
       print("Depósito realizado com sucesso!")
    else:
       print("Operação Falhou! Digite um valor válido.")
    return saldo, extrato
        
def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
       print("Operação falhou! Sem saldo suficiente.")

    elif numero_saques >= limite:
       print("Limite de valor de saque por operação excedido. Tente novamente")

    elif valor > limite:
       print("Operação falhou! Limite de saque excedido.")

    elif numero_saques >= limite_saques:
       print("Limite de saque diário excedido. Tente novamente amanhã!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque relizado com sucesso!")

    else:
        print("Saque não realizado. Saldo indisponível")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print("\nEXTRATO")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
       print("Usuário já cadastrado!")
       return usuarios

    nome = input("Informe o seu nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (formato: logradouro, numero, bairro, cidade/sigla Estado): ")
    
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    print("Usuário cadastrado com sucesso")
    return usuarios

def cadastrar_conta(agencia, contas, usuarios, proximo_numero_conta):
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
      print("Usuário não encontrado! Cadastre o usuário primeiro.")
      return agencia, contas, proximo_numero_conta

    numero_conta = proximo_numero_conta
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuarios[cpf]
    })
    print("Conta cadastrada com sucesso!")
    return agencia, contas, proximo_numero_conta + 1

def listar_contas(usuarios, contas):
    cpf = input("Informe o seu CPF (somente número): ")
    if cpf in usuarios:
     for conta in contas:
      if conta['usuario'] == usuarios[cpf]:
        print(f"Nome: {conta['usuario']['nome']},\nAgência: {conta['agencia']},\nConta: {conta['numero_conta']}")

    else:
        print("Sem cadastro neste CPF.")
    return(usuarios, contas)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = []
proximo_numero_conta = 1
agencia = "0001"

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato, 
            limite=limite, numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "c":
        agencia, contas, proximo_numero_conta = cadastrar_conta(agencia, contas, usuarios, proximo_numero_conta)

    elif opcao == "l":
        usuario, contas = listar_contas(usuarios, contas)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente.")