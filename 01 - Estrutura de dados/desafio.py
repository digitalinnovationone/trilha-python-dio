from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
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
            print("Operação falhou! Valor inválido.")
            return False

        if valor > self._saldo:
            print("Operação falhou! Saldo insuficiente.")
            return False

        self._saldo -= valor
        print("Saque realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! Valor inválido.")
            return False

        self._saldo += valor
        print("Depósito realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque"
            ]
        )

        if valor > self.limite:
            print("Operação falhou! Valor excede o limite.")
            return False

        if numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False
 
        return super().sacar(valor)

    def __str__(self):
        return f"""
Agência:\t{self.agencia}
Conta:\t\t{self.numero}
Titular:\t{self.cliente.nome}
Saldo:\t\tR$ {self.saldo:.2f}
"""


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


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
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


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


def menu():
    return """
================ MENU ================

[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas

[d] Depositar
[s] Sacar
[e] Extrato

[q] Sair

=> """


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return None

    return cliente.contas[0]


def criar_cliente(clientes):
    cpf = input("Informe o CPF: ").strip()

    if not cpf:
        print("CPF inválido.")
        return

    if filtrar_cliente(cpf, clientes):
        print("Já existe cliente com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco,
    )

    clientes.append(cliente)

    print("Cliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = ContaCorrente.nova_conta(
        cliente=cliente,
        numero=numero_conta,
    )

    cliente.adicionar_conta(conta)
    contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 40)
        print(conta)


def exibir_extrato(cliente):
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print("\n============== EXTRATO ==============")

    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")

    else:
        for transacao in conta.historico.transacoes:
            print(
                f"{transacao['data']} - "
                f"{transacao['tipo']}: "
                f"R$ {transacao['valor']:.2f}"
            )

    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("====================================")


clientes = []
contas = []

while True:
    opcao = input(menu()).lower()

    if opcao == "nu":
        criar_cliente(clientes)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "d":
        cpf = input("CPF do cliente: ")
        cliente = filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            continue

        conta = recuperar_conta_cliente(cliente)

        try:
            valor = float(input("Valor do depósito: "))
            cliente.realizar_transacao(conta, Deposito(valor))
        except ValueError:
            print("Digite um valor numérico válido.")

    elif opcao == "s":
        cpf = input("CPF do cliente: ")
        cliente = filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            continue

        conta = recuperar_conta_cliente(cliente)

        try:
            valor = float(input("Valor do saque: "))
            cliente.realizar_transacao(conta, Saque(valor))
        except ValueError:
            print("Digite um valor numérico válido.")

    elif opcao == "e":
        cpf = input("CPF do cliente: ")
        cliente = filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            continue

        exibir_extrato(cliente)

    elif opcao == "q":
        print("Encerrando sistema...")
        break

    else:
        print("Operação inválida.")
