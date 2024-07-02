import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.contas):
            raise StopIteration
        conta = self.contas[self._index]
        self._index += 1
        return f"Agência:\t{conta.agencia}\nNúmero:\t\t{conta.numero}\nTitular:\t{conta.cliente.nome}\nSaldo:\t\tR$ {conta.saldo:.2f}"


class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self._saldo = 0
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor <= 0 or valor > self._saldo:
            print("\n@@@ Operação falhou! Verifique o saldo ou o valor informado. @@@")
            return False
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor informado é inválido. @@@")
            return False
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques = [transacao for transacao in self.historico.transacoes if isinstance(transacao, Saque)]
        if len(saques) >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False
        if valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        return super().sacar(valor)

    def __str__(self):
        return f"Agência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": type(transacao).__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return func(*args, **kwargs)
    return envelope


def menu():
    return input(textwrap.dedent("""\
        ================ MENU ================
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        => """))


def buscar_cliente(cpf, clientes):
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Deposito(valor))


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if conta:
        print("\n================ EXTRATO ================")
        for transacao in conta.historico.transacoes:
            print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f} em {transacao['data']}")
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    if buscar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    clientes.append(Cliente(nome, cpf, endereco))
    print("\n=== Cliente criado com sucesso! ===")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 40)
        print(conta)


def main():
    clientes = []
    contas = []
    while (opcao := menu()) != 'q':
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'nc':
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        else:
            print("\n@@@ Operação inválida! @@@")

if __name__ == "__main__":
    main()
