import random

home = """
============ Banco Py ===========

Bem vindo os sistema do Banco Py

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
    
    for dados in contas_ativas:
        if dados["agencia"] == ag and dados["conta"] == cc :
            print("passou na ag e cc ")
            senhaHash = input("Digite sua senha: ")
            if senhaHash == dados["senha"]:
                print(f"\n SEJA BEM VINSO A SUA CONTA \n {dados['nome']} \n")
                    ## Aqui devemos chamar as funçoes da conta ativa... 
                    #break
        else:
            print("\nNão Achamos sua conta no nosso sistema.")
            print(contas_ativas)
            diretriz()
                #break
            
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

inicio()