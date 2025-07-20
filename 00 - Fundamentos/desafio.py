from datetime import datetime, date
from abc import ABC, abstractmethod

# ======== CONSTANTES ======== 
LIMITE_SAQUE = 500 
LIMITE_SAQUES_DIARIOS = 3 

# ======== CLASSES ========

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def cpf(self):
        return self._cpf
        
    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def historico(self):
        return self._historico
        
    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido. Saque apenas valores positivos.")
            return False
            
        if valor > self._saldo:
            print("❌ Saldo insuficiente.")
            return False
            
        self._saldo -= valor
        print("✅ Saque realizado com sucesso.")
        return True
        
    def depositar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido. Deposite apenas valores positivos.")
            return False
            
        self._saldo += valor
        print("✅ Depósito realizado com sucesso.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=LIMITE_SAQUE, limite_saques=LIMITE_SAQUES_DIARIOS):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0
        
    def sacar(self, valor):
        if valor > self._limite:
            print(f"❌ Saque excede o limite de R$ {self._limite}.")
            return False
            
        if self._saques_realizados >= self._limite_saques:
            print("❌ Limite diário de saques atingido.")
            return False
            
        sucesso = super().sacar(valor)
        if sucesso:
            self._saques_realizados += 1
        return sucesso

# ======== ESTADOS GLOBAIS ======== 
clientes = []
contas = []

# ======== FUNÇÕES AUXILIARES ======== 

def encontrar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def encontrar_conta_por_cliente(cliente):
    for conta in contas:
        if conta.cliente == cliente:
            return conta
    return None

def listar_contas():
    for conta in contas:
        print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {conta.cliente.nome}")

# ======== FUNÇÕES DE USUÁRIO E CONTA ======== 

def criar_cliente():
    cpf = input("Informe o CPF (somente números): ").strip()
    if encontrar_cliente_por_cpf(cpf):
        print("❌ Já existe um cliente com esse CPF.")
        return None

    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço (logradouro, número, bairro, cidade/UF): ").strip()

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("✅ Cliente criado com sucesso!")
    return cliente

def criar_conta_corrente(cliente):
    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"✅ Conta criada com sucesso! Agência: {conta.agencia} Conta: {conta.numero}")
    return conta

# ======== OPERAÇÕES DO CLIENTE LOGADO ======== 

def menu_operacoes(cliente, conta):
    menu = f"""
Bem-vindo(a), {cliente.nome}!
=============== MENU BANCÁRIO ===============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    while True:
        opcao = input(menu).lower().strip()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                transacao = Deposito(valor)
                cliente.realizar_transacao(conta, transacao)
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                transacao = Saque(valor)
                cliente.realizar_transacao(conta, transacao)
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================\n")
            if not conta.historico.transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for transacao in conta.historico.transacoes:
                    print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("👋 Obrigado por utilizar nosso sistema. Até a próxima!")
            break

        else:
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")

# ======== MENU INICIAL DO SISTEMA ======== 

def menu_inicial():
    while True:
        print("\n====== BEM-VINDO AO BANCO PYTHON ======")
        cpf = input("Já é nosso cliente? Insira seu CPF (ou pressione Enter para sair): ").strip()

        if not cpf:
            print("Saindo do sistema. Até logo!")
            break

        cliente = encontrar_cliente_por_cpf(cpf)

        if cliente:
            conta = encontrar_conta_por_cliente(cliente)
            if conta:
                menu_operacoes(cliente, conta)
            else:
                print("⚠️ Cliente encontrado, mas sem conta ativa.")
                criar = input("Deseja criar uma conta agora? (s/n): ").lower()
                if criar == "s":
                    conta = criar_conta_corrente(cliente)
                    menu_operacoes(cliente, conta)
                else:
                    print("Conta não criada. Retornando ao menu inicial.")
        else:
            print("❌ Cliente não encontrado.")
            criar = input("Deseja se cadastrar como novo cliente? (s/n): ").lower()
            if criar == "s":
                novo_cliente = criar_cliente()
                if novo_cliente:
                    conta = criar_conta_corrente(novo_cliente)
                    menu_operacoes(novo_cliente, conta)
            else:
                print("Cadastro não realizado. Retornando ao menu.")

# ======== EXECUÇÃO ======== 
if __name__ == "__main__":
    menu_inicial()