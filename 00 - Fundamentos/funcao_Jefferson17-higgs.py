#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema Bancário com:
- Cadastro de usuários
- Criação de contas correntes
- Operações bancárias
"""

# Estruturas de dados globais
usuarios = []
contas = []
numero_conta_sequencial = 1

def criar_usuario(nome, data_nascimento, cpf, endereco, /):
    """
    Cria um novo usuário (positional-only parameters)
    
    Args:
        nome (str): Nome completo do usuário
        data_nascimento (str): Data de nascimento no formato DD/MM/AAAA
        cpf (str): CPF do usuário (somente números)
        endereco (str): Endereço no formato: logradouro, nro - bairro - cidade/UF
        
    Returns:
        dict: Dicionário com os dados do usuário criado ou None se CPF já existir
    """
    global usuarios
    
    # Verifica se CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\nErro: Já existe um usuário com este CPF!")
        return None
    
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(novo_usuario)
    print("\nUsuário criado com sucesso!")
    return novo_usuario

def criar_conta_corrente(*, cpf_usuario):
    """
    Cria uma nova conta corrente (keyword-only parameter)
    
    Args:
        cpf_usuario (str): CPF do usuário para vincular à conta
        
    Returns:
        dict: Dicionário com os dados da conta criada ou None se usuário não existir
    """
    global contas, numero_conta_sequencial
    
    # Busca usuário pelo CPF
    usuario = next((u for u in usuarios if u['cpf'] == cpf_usuario), None)
    
    if not usuario:
        print("\nErro: Usuário não encontrado! Cadastre o usuário primeiro.")
        return None
    
    nova_conta = {
        'agencia': '0001',
        'numero_conta': numero_conta_sequencial,
        'usuario': usuario,
        'saldo': 0.0,
        'extrato': '',
        'limite_saques': 0
    }
    
    contas.append(nova_conta)
    numero_conta_sequencial += 1
    print(f"\nConta criada com sucesso! Número: {nova_conta['numero_conta']}")
    return nova_conta

# Funções existentes (adaptadas para trabalhar com contas)
def deposito(conta, valor, /):
    """Realiza depósito na conta especificada (positional-only)"""
    if valor <= 0:
        return "Valor inválido para depósito."
    
    conta['saldo'] += valor
    conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
    return f"Depósito realizado. Saldo atual: R$ {conta['saldo']:.2f}"

def saque(*, conta, valor):
    """Realiza saque na conta especificada (keyword-only)"""
    if valor <= 0:
        return "Valor de saque inválido."
    if valor > 500:
        return "Limite de R$ 500.00 por saque excedido."
    if conta['limite_saques'] >= 3:
        return "Limite diário de saques excedido."
    if valor > conta['saldo']:
        return "Saldo insuficiente."
    
    conta['saldo'] -= valor
    conta['limite_saques'] += 1
    conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
    return f"Saque realizado. Saldo atual: R$ {conta['saldo']:.2f}"

def extrato(conta, /, *, detalhado=False):
    """Exibe extrato da conta (positional-only e keyword-only)"""
    print('\n' + ' EXTRATO '.center(27, '-'))
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    if detalhado:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
    print('-' * 27 + '\n')

# Menu principal
def menu_principal():
    while True:
        print('\n' + ' MENU PRINCIPAL '.center(30, '='))
        print("""
        1. Criar Usuário
        2. Criar Conta Corrente
        3. Selecionar Conta
        4. Listar Contas
        5. Sair
        """)
        opcao = input("Opção => ").strip()
        
        if opcao == '1':
            print('\n' + ' NOVO USUÁRIO '.center(30, '-'))
            nome = input("Nome completo: ").strip()
            data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
            cpf = input("CPF (somente números): ").strip()
            endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()
            criar_usuario(nome, data_nasc, cpf, endereco)
            
        elif opcao == '2':
            if not usuarios:
                print("\nNenhum usuário cadastrado. Crie um usuário primeiro.")
                continue
                
            print('\n' + ' NOVA CONTA '.center(30, '-'))
            cpf = input("CPF do titular (somente números): ").strip()
            criar_conta_corrente(cpf_usuario=cpf)
            
        elif opcao == '3':
            if not contas:
                print("\nNenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
                
            conta = selecionar_conta()
            if conta:
                menu_conta(conta)
                
        elif opcao == '4':
            listar_contas()
            
        elif opcao == '5':
            print("\nSistema encerrado. Até logo!")
            break
            
        else:
            print("\nOpção inválida! Tente novamente.")

# Funções auxiliares
def selecionar_conta():
    """Permite selecionar uma conta existente"""
    print('\n' + ' SELECIONAR CONTA '.center(30, '-'))
    cpf = input("Digite seu CPF: ").strip()
    
    contas_usuario = [c for c in contas if c['usuario']['cpf'] == cpf]
    
    if not contas_usuario:
        print("\nNenhuma conta encontrada para este CPF.")
        return None
        
    if len(contas_usuario) == 1:
        return contas_usuario[0]
        
    print("\nContas encontradas:")
    for i, conta in enumerate(contas_usuario, 1):
        print(f"{i} - Ag {conta['agencia']} C/C {conta['numero_conta']}")
    
    while True:
        try:
            escolha = int(input("\nSelecione a conta: ")) - 1
            if 0 <= escolha < len(contas_usuario):
                return contas_usuario[escolha]
            print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_conta(conta):
    """Menu de operações para uma conta específica"""
    while True:
        print('\n' + f" CONTA {conta['agencia']}/{conta['numero_conta']} ".center(30, '-'))
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print("""
        1. Depositar
        2. Sacar
        3. Extrato
        4. Extrato Detalhado
        5. Voltar
        """)
        opcao = input("Opção => ").strip()
        
        if opcao == '1':
            print('\n' + ' DEPÓSITO '.center(20, '-'))
            try:
                valor = float(input("Valor a depositar: R$ "))
                print(deposito(conta, valor))
            except ValueError:
                print("Valor inválido!")
                
        elif opcao == '2':
            print('\n' + ' SAQUE '.center(20, '-'))
            try:
                valor = float(input("Valor a sacar: R$ "))
                print(saque(conta=conta, valor=valor))
            except ValueError:
                print("Valor inválido!")
                
        elif opcao == '3':
            extrato(conta)
            
        elif opcao == '4':
            extrato(conta, detalhado=True)
            
        elif opcao == '5':
            break
            
        else:
            print("Opção inválida!")

def listar_contas():
    """Lista todas as contas cadastradas"""
    print('\n' + ' CONTAS CADASTRADAS '.center(50, '='))
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print(f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        CPF:\t\t{conta['usuario']['cpf']}
        Saldo:\t\tR$ {conta['saldo']:.2f}
        """ + '-'*50)

# Inicialização do sistema
if __name__ == "__main__":
    menu_principal()