from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime 
import textwrap

class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._agencia = "0001"
        self._saldo = 0
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
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Déposito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao['tipo'] == "saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excedeu o limite! @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido! @@@")    

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        C/C:\t{self.numero}
        Titular:\t{self.cliente.nome}
        Saldo:\tR$ {self.saldo:.2f}
        """
class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y/%H:%M:%S")
        })

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\n
    =======================
    |    MENU DE OPÇÕES   |
    =======================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Cliente
    [5]\tNova Conta
    [6]\tListar Contas
    [0]\tSair
    =>"""

    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ O cliente não possui conta! @@@")
        return 
    
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))

    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao) 

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))

    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao) 

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato += "\nNão foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}\tR$ {transacao['valor']:.2f}\t{transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}") 

def criar_cliente(clientes):
    cpf = input("Informe o cpf (somente numeros): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n @@@ Já existe esse cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo do cliente: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n === Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n === Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("-" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)
        elif opcao == "2":
            sacar(clientes)
        elif opcao == "3":
            exibir_extrato(clientes)
        elif opcao == "4":
            criar_cliente(clientes)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            print("""
    ============================================
    |  Obrigado por utilizar o nosso sistema!  |
    ============================================""")
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()