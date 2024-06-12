import  datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Criar usuário
[cc] Criar conta
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques_no_dia = 0
LIMITE_SAQUES = 3
data_ultimo_saque = datetime.date.today()
print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
usuarios = []
contas = []
numero_da_conta = 0

def saque (*,saldo,extrato,limite,numero_saques_no_dia,LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques_no_dia >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        global data_ultimo_saque,data_ultimo_saque
        if data_ultimo_saque != datetime.date.today():
            data_ultimo_saque = datetime.date.today()
            numero_saques_no_dia = 1
        else: numero_saques_no_dia += 1
        linha = '='

        titulo = 'SAQUE'
        print("\n", titulo.center(50, '='))
        print("Saque realizado com sucesso!")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(50 * '=')
    else:
        print("Operação falhou! O valor informado é inválido.")   
    return saldo,extrato
def deposito (saldo,extrato):
   valor = float(input("Informe o valor do depósito: "))
   if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
   else:
        print("Operação falhou! O valor informado é inválido.")
   return saldo,extrato
def extrato (saldo,/,*,extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
def criar_usuario(usuarios):
    #global usuarios
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario :
        print("cpf já cadastrado")
        return
    
    nome = input("Informe o nome do novo usuário: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: logradouro, nro - bairro - cidade/estado: ")
    usuarios.append ({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})    
def criar_conta_corrente():
    #global contas
    cpf = input("Informe o cpf: ")
    global numero_da_conta
    if filtrar_usuario(cpf,usuarios):
        contas.append ({"agencia":'0001',"conta":numero_da_conta,"cpf":cpf})
        numero_da_conta += 1
        print("agencia:0001", "conta: ", numero_da_conta,"cpf: ",cpf)
    else:
        print("cpf não cadastrado")
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
while True:
    #print(f"Saldo atual: {saldo:.2f}")
    opcao = input(menu.lower())

    if opcao == "d":
        saldo,extrato = deposito (saldo,extrato)
    elif opcao == "c":
        criar_usuario(usuarios=usuarios)
    elif opcao == "cc":
        criar_conta_corrente()
    elif opcao == "s":
        saldo,extrato =saque(saldo = saldo,extrato=extrato,limite=limite,numero_saques_no_dia=numero_saques_no_dia,LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == "e":
        extrato (saldo,extrato=extrato)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
