from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

class Conta:
    agencia_padrao = "0001"

    def __init__(self, cliente, nro_conta):
        self._saldo = 0
        self._nro_conta = nro_conta
        self._cliente = cliente
        self._agencia = self.agencia_padrao
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, nro_conta):
        return cls(cliente, nro_conta)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def nro_conta(self):
        return self._nro_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Valor de depósito inválido.")
            return False
        
    def sacar(self, valor):
        if valor > self._saldo:
            print("Operação falhou! Sem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor não é válido.")
        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, nro_conta, limite=500, limite_saques=3):
        super().__init__(cliente, nro_conta)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        num_saques = len([transacao for transacao in self.historico.transacoes
                          if transacao["tipo"] == "Saque"])

        if valor > self._limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif num_saques >= self._limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t{self.nro_conta}
Titular:\t{self.cliente.nome}
        """

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
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

class Transacao(ABC):
    @property
    @abstractmethod
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

def display_menu():
    menu = """\n
    =============MENU=============
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [lc] Lista Contas
    [q] Sair
    => """
    return input(menu)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta cadastrada")
        return None
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Digite o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Digite o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("\n============ EXTRATO ============")
    transacoes = conta.historico.transacoes
    extrato = "Não foram realizadas movimentações." if not transacoes else ""
    for transacao in transacoes:
        extrato += f"\n{transacao['tipo']}: R${transacao['valor']:.2f} em {transacao['data']}"
    print(extrato)
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("====================================")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado. Conta não cadastrada!")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, nro_conta=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))

def criar_cliente(clientes):
    cpf = input("Informe seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("CPF já cadastrado!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro, bairro, cidade/sigla Estado): ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def main():
    clientes = []
    contas = []
    while True:
        opcao = display_menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida! Selecione uma das opções disponíveis.")
            
if __name__ == "__main__":
    main()
