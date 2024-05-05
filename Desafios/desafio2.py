import random

home = """
============ Banco Py ===========

Bem vindo os sistema do Banco Py

=================================
"""

menu = """
============ Banco Py ===========
Seleciona a opção: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=================================
"""

## AGÊNCIAS PRÉ DEFINIDAS PELO BANCO
AGENCIAS_VALIDAS = ["0001", "0010", "0101", "1234"]

## CONTAS JA CADASTRADOS NO BANCO, PODENDO SER ADICIONADO MAIS CONTAS
contas_ativas = [
    {
        "agencia": "0001",
        "conta": "001201",
        "senha": "1515",
        "nome": "Gabriel"
    }
]

transacoes = []

sessao = False

## PRÉ DEFINIÇÃO DE FORMATO DE DADOS DAS CONTAS
def novaConta(agencia, conta, senha, nome):
    return {
        "agencia": agencia,
        "conta": conta,
        "senha": senha,
        "nome": nome
    }

## VERIFICA SE OS DADOS EXISTEM EM UMA LISTA PRÉ DEFINIDA ANTERIORMENTE
def vefiricaDados(item, verificar):

    if item in verificar:
        return True
    else: return False

## CASO TENHA ERRO OU INCONSISTÊNCIA NAS ENTRADAS, CHAMOS ESTA FUNÇÃO 
def diretriz():
    if sessao == False:
        op = input("""
============= OPÇÕES ============

DESEJA CRIAR UMA CONTA?
[s] SIM
[n] NÃO
               
[i] Voltar ao início
[q] Sair

=================================
""")
        if op == "s": 
            criarCont()
        elif op == "i":
            inicio()
        elif op == "n" or op == "q": 
            print("Obrigado por acessar nossos serviços!") 
            print("\n=================================")
            quit()
        else: print("Opção inválida!")
    else:  
        sessaoConta()

## FUNÇÃO PARA CRIAR UMA NOVA CONTA, VERIFICAR SE A SENHA CRIADA É VÁLIDA
## ADICIONANDO A NOVA CONTA AO BANCO DE DADOS
def criarCont():
    print("""=================================
            CRIAR CONTA
=================================""")

    global contas_ativas

    ## DE FORMA ALEATÓRIA ESCOLHE OS DIGITOS DA CONTA DO NOVO CLIENTE
    cc = random.randint(100, 1000)
    conta = str(cc).zfill(6)

    ## DE FORMA ALEATÓRIA ESCOLHE UMA AGENCIA PARA O CLIENTE
    ag = random.randint(0, 3)
    agencia = AGENCIAS_VALIDAS[ag]

    nome = input("Qual seu nome: \n")
    senha = input("Vamos criar uma senha com 4 digitos: \n")

    ## VERIFICAÇÃO DE SENHA PARA A NOVA CONTA
    while True:
        if senha != input("Digite a senha novamente: \n"):
            print("As senhas nao são iguais, tente novamente.")
        else: 
            ## ADICIONA A NOVA CONTA AO BANCO DE DADOS
            contas_ativas.append(novaConta(agencia, conta, senha, nome))
            print(f""" =================================
    CONTA CRIADA COM SUCESSO
                  
    Nome: {nome}
    Agência: {agencia}
    Conta: {conta}

 *Guarde os dados com segurança*

=================================""")
            break
    inicio()

## VERIFICA O ACESSO A CONTA, COM BASE NO BANCO DE DADOS,
def acessaConta(ag, cc):

    global contas_ativas
    global sessao
    
    for dados in contas_ativas:
        if dados["agencia"] == ag and dados["conta"] == cc :
            print("passou na ag e cc ")
            senhaHash = input("Digite sua senha: ")
            if senhaHash == dados["senha"]:
                print(f"\n SEJA BEM VINSO A SUA CONTA \n {dados['nome']} \n")
                sessao = True
                sessaoConta()

            else:
                print("\nNão Achamos sua conta no nosso sistema.")
                print(contas_ativas)
                # diretriz()
            
## INÍCIO DO NOSSO SISTEMA
def inicio():
    print(home)
    print("\nEntre com os dados da sua Agência e conta. \nNão incluia traços e/ou pontos, apenas numeros. ")

    while True:
        agencia = input("Digite sua agencia com 4 digitos: ")
        if agencia.isdigit() and len(agencia) == 4:

            if vefiricaDados(agencia, AGENCIAS_VALIDAS):

                conta = input("Digite o numero da conta con 6 digitos: ")
                if conta.isdigit() and len(conta) == 6:
                    acessaConta(agencia, conta)
                    break

            else: 
                print("A agencia digitada nao pertence a nosso Banco.\n")
                diretriz()
                break
        else:
            print("Erro, tente novamente uma agencia válida. \n São 4 digitos numericos.")

def operacao(tipo, valor):
    global transacoes
    codigo = (f"{tipo}{len(transacoes) +1}", f"R$ {valor}")
    transacoes.append(codigo)
    #print(transacoes)

def sessaoConta():
    global menu

    saldo = 0
    limiteSaque = 500
    extrato = ""
    numSaque = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            print("Deposito")
            deposito = float(input("Informe o valor de Depsito: R$ ").replace(',','.'))
            while deposito < 1:
                print("Deposito inválido. Insira um valor de deposito válido, acima de R$ 1.00 .")
                deposito = float(input("Informe o valor de Depsito: R$ ").replace(',','.'))
            else:
                operacao("D", deposito)
                saldo += deposito
    
        elif opcao == "s":
            print("Saque")
            if numSaque == LIMITE_SAQUES:
                print("Você atingiu o limite de saque diário.")
        
            elif saldo == 0:
                print("Você nao possue saldo suficiente para saque! Faça um deposito. :) ")
            else:
                saque = float(input("Informe o valor de Saque: R$ ").replace(',','.'))

                if saque > limiteSaque or saque < 1:
                    print("O valo máximo para saque é entre R$ 1,00 a R$ 500.00.\n Tente novamente com um novo valor.")

                else:
                    if saque <= saldo and saque <= limiteSaque and numSaque < LIMITE_SAQUES:
                        saldo -= saque
                        numSaque += 1
                        operacao("S", saque)
                    else:
                        print("Operação inválida... Consulte saldo disponível para saque!")

        elif opcao == "e":
            print("Extrato")
            for dados in transacoes: print(dados, sep="\n")
            print(f"\nSaldo Atual: R$ {saldo:.2f}")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


## INICIAMOS O NOSSO SISTEMA...    
inicio()