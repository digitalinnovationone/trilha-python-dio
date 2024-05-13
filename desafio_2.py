import textwrap



def menu():
    menu = """

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [u] Novo Usuario
            [c] Criar Conta
            [l] Listar Contas
            [q] Sair

            => """
    return input(textwrap.dedent(menu))



def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
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
    
    return saldo, extrato


def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cria_usuario(lista_usuario, lista_aux):
    cpf = int(input("Digite o CPF(somente números): "))
    if cpf in lista_aux:
        print("Usuario ja cadastrado!")
    else:
        nome = input("Digite o nome completo: ")
        data_nascimento = input("Entre com a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Entre com o endereço (logradouro, nro - bairro - cidade/estado): ")

        lista_usuario.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})
        lista_aux.append(cpf)
        print("Usuario cadastrado com sucesso")
        

def criar_conta(lista_aux, lista_contas, agencia, num_conta):
    cpf = int(input("Digite o CPF(somente números): "))
    if cpf not in lista_aux:
        print("Usuario não cadastrado")
    else:
        print("Conta criada com sucesso!")
        
        lista_contas.append({"cpf": cpf, "agencia": agencia, "numero_conta": num_conta})
        print(lista_contas)

def listar_contas(lista_contas):
    for l in lista_contas:
        linha = f"""Ag: {l['agencia']}
                    Conta: {l['numero_conta']} 
                    Usuario: {l['cpf']} """
        print(linha)






def main():

    agencia = "0001"
    lista_usuario = []
    lista_aux = []
    lista_contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    num_conta = 0

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)

        elif opcao == "e":
            extrato(saldo,extrato=extrato)

        elif opcao == "u":
            cria_usuario(lista_usuario, lista_aux)
    
        elif opcao == "c":
            num_conta += 1
            criar_conta(lista_aux, lista_contas, agencia, num_conta)
            
        elif opcao == "l":
            criar_conta(lista_contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
