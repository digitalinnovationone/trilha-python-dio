import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_transacao(self, conta, operacao):
        operacao.processar(conta)

    def vincular_conta(self, conta):
        self.contas.append(conta)


class Pessoa(Usuario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf


class ContaBancaria:
    def __init__(self, numero, usuario):
        self._numero = numero
        self._usuario = usuario
        self._agencia = "0001"
        self._saldo = 0.0
        self._historico = RegistroOperacoes()

    @classmethod
    def criar_conta(cls, usuario, numero):
        return cls(numero, usuario)

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
        return self._usuario

    @property
    def historico(self):
        return self._historico

    def sacar(self, quantia):
        if quantia <= 0:
            print("\n@@@ Valor inválido para saque. @@@")
            return False

        if quantia > self._saldo:
            print("\n@@@ Saldo insuficiente. @@@")
            return False

        self._saldo -= quantia
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, quantia):
        if quantia <= 0:
            print("\n@@@ Valor inválido para depósito. @@@")
            return False

        self._saldo += quantia
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(ContaBancaria):
    def __init__(self, numero, usuario, limite=500, saques_disponiveis=3):
        super().__init__(numero, usuario)
        self._limite = limite
        self._saques_disponiveis = saques_disponiveis

    def sacar(self, quantia):
        saques_realizados = len(
            [op for op in self.historico.transacoes if op["tipo"] == Saque.__name__]
        )

        if quantia > self._limite:
            print("\n@@@ Limite de saque excedido. @@@")
            return False

        if saques_realizados >= self._saques_disponiveis:
            print("\n@@@ Limite de saques atingido. @@@")
            return False

        return super().sacar(quantia)

    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        Conta:\t\t{self.numero}
        Cliente:\t{self.cliente.nome}
        """


class RegistroOperacoes:
    def __init__(self):
        self._eventos = []

    @property
    def transacoes(self):
        return self._eventos

    def registrar(self, operacao):
        self._eventos.append({
            "tipo": operacao.__class__.__name__,
            "valor": operacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Operacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def processar(self, conta):
        pass


class Saque(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def processar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.registrar(self)


class Deposito(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def processar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.registrar(self)


# Funções auxiliares
def menu():
    opcoes = """\n
    ======== MENU PRINCIPAL ========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair
    => """
    return input(textwrap.dedent(opcoes))


def localizar_cliente(cpf, lista_clientes):
    return next((c for c in lista_clientes if c.cpf == cpf), None)


def selecionar_conta(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente ainda não possui conta bancária. @@@")
        return None
    return cliente.contas[0]  # pode ser adaptado para permitir escolha


def criar_usuario(lista_usuarios):
    cpf = input("CPF: ")
    if localizar_cliente(cpf, lista_usuarios):
        print("\n@@@ CPF já cadastrado. @@@")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, número - bairro - cidade/UF): ")

    novo_usuario = Pessoa(nome, nascimento, cpf, endereco)
    lista_usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucesso! ===")


def abrir_conta(num_conta, lista_usuarios, lista_contas):
    cpf = input("CPF do usuário: ")
    usuario = localizar_cliente(cpf, lista_usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado. @@@")
        return

    conta = ContaCorrente.criar_conta(usuario, num_conta)
    lista_contas.append(conta)
    usuario.vincular_conta(conta)

    print("\n=== Conta aberta com sucesso! ===")


def mostrar_contas(lista_contas):
    for conta in lista_contas:
        print("=" * 80)
        print(str(conta))


def executar_deposito(lista_usuarios):
    cpf = input("CPF do cliente: ")
    usuario = localizar_cliente(cpf, lista_usuarios)

    if not usuario:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    conta = selecionar_conta(usuario)
    if not conta:
        return

    valor = float(input("Valor do depósito: "))
    op = Deposito(valor)
    usuario.executar_transacao(conta, op)


def executar_saque(lista_usuarios):
    cpf = input("CPF do cliente: ")
    usuario = localizar_cliente(cpf, lista_usuarios)

    if not usuario:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    conta = selecionar_conta(usuario)
    if not conta:
        return

    valor = float(input("Valor do saque: "))
    op = Saque(valor)
    usuario.executar_transacao(conta, op)


def ver_extrato(lista_usuarios):
    cpf = input("CPF do cliente: ")
    usuario = localizar_cliente(cpf, lista_usuarios)

    if not usuario:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    conta = selecionar_conta(usuario)
    if not conta:
        return

    print("\n========== EXTRATO ==========")
    historico = conta.historico.transacoes

    if not historico:
        print("Nenhuma movimentação realizada.")
    else:
        for item in historico:
            print(f"{item['tipo']}:\tR$ {item['valor']:.2f} ({item['data']})")

    print(f"\nSaldo disponível:\tR$ {conta.saldo:.2f}")
    print("=============================")


# Execução principal
def main():
    usuarios = []
    contas = []

    while True:
        escolha = menu()

        if escolha == "d":
            executar_deposito(usuarios)
        elif escolha == "s":
            executar_saque(usuarios)
        elif escolha == "e":
            ver_extrato(usuarios)
        elif escolha == "nu":
            criar_usuario(usuarios)
        elif escolha == "nc":
            abrir_conta(len(contas) + 1, usuarios, contas)
        elif escolha == "lc":
            mostrar_contas(contas)
        elif escolha == "q":
            print("\n=== Encerrando o sistema. ===")
            break
        else:
            print("\n@@@ Opção inválida. Tente novamente. @@@")

# Iniciar sistema
main()
