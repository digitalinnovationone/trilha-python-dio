import textwrap
from datetime import datetime
from abc import ABC, abstractmethod

# ==== CLASSES DO SISTEMA ====

# Representa o cliente do banco
class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco  # Onde o cliente mora
        self.contas = []  # Lista de contas bancárias que ele possui

    # Serve para registrar uma operação (como saque ou depósito)
    def registrar_movimento(self, conta, operacao):
        if len(conta.atividades.transacoes_do_dia()) >= 2:
            print("\n!!! Limite de transações diárias atingido !!!")
            return
        operacao.aplicar(conta)

    # Adiciona uma nova conta para o cliente
    def vincular_conta(self, nova_conta):
        self.contas.append(nova_conta)

# Cliente com nome, data de nascimento e CPF
class Pessoa(Usuario):
    def __init__(self, nome_completo, nascimento, doc_id, endereco):
        super().__init__(endereco)
        self.nome = nome_completo
        self.data_nasc = nascimento
        self.cpf = doc_id


# Conta básica do banco (modelo genérico)
class ContaBancaria:
    def __init__(self, codigo, dono):
        self._disponivel = 0  # Saldo da conta
        self._codigo = codigo  # Número da conta
        self._ag = "0001"  # Agência fixa
        self._titular = dono  # Quem é o dono da conta
        self._atividades = Registro()  # Histórico de transações

    @classmethod
    def criar(cls, dono, codigo):
        return cls(codigo, dono)

    # Abaixo estão os "atalhos" (propriedades) para acessar os dados
    @property
    def saldo(self):
        return self._disponivel

    @property
    def codigo(self):
        return self._codigo

    @property
    def agencia(self):
        return self._ag

    @property
    def titular(self):
        return self._titular

    @property
    def atividades(self):
        return self._atividades

    # Método para fazer saque
    def retirar(self, quantia):
        if quantia > self.saldo:
            print("\n!!! Saldo insuficiente !!!")
        elif quantia <= 0:
            print("\n!!! Valor inválido para saque !!!")
        else:
            self._disponivel -= quantia
            print("\n>>> Saque efetuado com sucesso!")
            return True
        return False

    # Método para fazer depósito
    def adicionar(self, quantia):
        if quantia > 0:
            self._disponivel += quantia
            print("\n>>> Depósito realizado com sucesso!")
            return True
        else:
            print("\n!!! Valor de depósito inválido !!!")
            return False


# Conta com regras específicas, como limite e número máximo de saques
class ContaCorrente(ContaBancaria):
    def __init__(self, codigo, dono, maximo=500, limite_operacoes=3):
        super().__init__(codigo, dono)
        self._limite = maximo  # Valor máximo por saque
        self._max_operacoes = limite_operacoes  # Número máximo de saques

    @classmethod
    def criar(cls, dono, codigo, maximo, limite_operacoes):
        return cls(codigo, dono, maximo, limite_operacoes)

    # Reescrevendo o método de saque para aplicar as regras da conta corrente
    def retirar(self, quantia):
        total_saques = len([
            mov for mov in self.atividades.transacoes
            if mov["tipo"] == Retirada.__name__
        ])

        if quantia > self._limite:
            print("\n!!! Saque excede limite permitido por operação !!!")
        elif total_saques >= self._max_operacoes:
            print("\n!!! Número de saques excedido para hoje !!!")
        else:
            return super().retirar(quantia)

        return False

    # Como o objeto aparece quando você imprime ele
    def __str__(self):
        return f"""\
        Agência: {self.agencia}
        Conta: {self.codigo}
        Cliente: {self.titular.nome}
        """


# Guarda todas as transações feitas na conta
class Registro:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    # Adiciona uma transação no histórico
    def gravar(self, movimento):
        self._transacoes.append({
            "tipo": movimento.__class__.__name__,
            "valor": movimento.valor,
            "momento": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

    # Gera uma lista com todas ou algumas transações (filtradas)
    def gerar_extrato(self, tipo=None):
        for item in self._transacoes:
            if tipo is None or item["tipo"].lower() == tipo.lower():
                yield item

    # Retorna só as transações feitas no dia atual
    def transacoes_do_dia(self):
        hoje = datetime.datetime.now().date()
        return [
            mov for mov in self._transacoes
            if datetime.strptime(mov["momento"], "%d-%m-%Y %H:%M:%S").date() == hoje
        ]


# ==== CLASSES DE TRANSAÇÕES (Saque / Depósito) ====

class Movimento(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def aplicar(self, conta):
        pass

# Classe para saque
class Retirada(Movimento):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def aplicar(self, conta):
        sucesso = conta.retirar(self.valor)
        if sucesso:
            conta.atividades.gravar(self)

# Classe para depósito
class Aporte(Movimento):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def aplicar(self, conta):
        sucesso = conta.adicionar(self.valor)
        if sucesso:
            conta.atividades.gravar(self)


# ==== FUNÇÕES AUXILIARES ==== #

def menu():
    opcoes = """\n
    ======= OPÇÕES DISPONÍVEIS ========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo cliente
    [5] Nova conta
    [6] Contas cadastradas
    [0] Encerrar
    => """
    return input(textwrap.dedent(opcoes))

# Procura um cliente pelo CPF
def localizar_usuario(doc_id, usuarios):
    filtrados = [u for u in usuarios if u.cpf == doc_id]
    return filtrados[0] if filtrados else None

# Pega a primeira conta de um cliente
def acessar_conta(usuario):
    if not usuario.contas:
        print("\n!!! Cliente não possui conta cadastrada !!!")
        return None
    return usuario.contas[0]

# Faz um depósito
def fazer_deposito(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = localizar_usuario(cpf, clientes)

    if not cliente:
        print("\n!!! CPF não encontrado !!!")
        return

    valor = float(input("Valor a depositar: "))
    transacao = Aporte(valor)
    conta = acessar_conta(cliente)

    if conta:
        cliente.registrar_movimento(conta, transacao)

# Faz um saque
def fazer_saque(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = localizar_usuario(cpf, clientes)

    if not cliente:
        print("\n!!! CPF não encontrado !!!")
        return

    valor = float(input("Valor a sacar: "))
    transacao = Retirada(valor)
    conta = acessar_conta(cliente)

    if conta:
        cliente.registrar_movimento(conta, transacao)

# Mostra o extrato da conta
def mostrar_extrato(clientes):
    cpf = input("CPF do cliente: ")
    cliente = localizar_usuario(cpf, clientes)

    if not cliente:
        print("\n!!! CPF não encontrado !!!")
        return

    conta = acessar_conta(cliente)

    if not conta:
        return

    print("\n======== EXTRATO ==========")
    transacoes = list(conta.atividades.gerar_extrato())
    if not transacoes:
        print("Sem movimentações registradas.")
    else:
        for t in transacoes:
            print(f"{t['momento']} | {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("============================")

# Cadastra um novo cliente
def criar_usuario(clientes):
    cpf = input("CPF (apenas números): ")
    if localizar_usuario(cpf, clientes):
        print("\n!!! Cliente já cadastrado com este CPF !!!")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, número - bairro - cidade/UF): ")

    novo = Pessoa(nome_completo=nome, nascimento=nascimento, doc_id=cpf, endereco=endereco)
    clientes.append(novo)
    print("\n>>> Novo cliente registrado com sucesso!")

# Cria uma nova conta para um cliente existente
def criar_nova_conta(numero, clientes, contas):
    cpf = input("CPF do titular: ")
    cliente = localizar_usuario(cpf, clientes)

    if not cliente:
        print("\n!!! CPF não encontrado. Conta não criada. !!!")
        return

    conta = ContaCorrente.criar(cliente, numero, maximo=500, limite_operacoes=3)
    contas.append(conta)
    cliente.vincular_conta(conta)
    print("\n>>> Conta aberta com sucesso!")

# Lista todas as contas criadas
def listar_todas(contas):
    for conta in contas:
        print("=" * 40)
        print(str(conta))


# ==== FUNÇÃO PRINCIPAL (MENU) ====
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            fazer_deposito(clientes)
        elif opcao == "2":
            fazer_saque(clientes)
        elif opcao == "3":
            mostrar_extrato(clientes)
        elif opcao == "4":
            criar_usuario(clientes)
        elif opcao == "5":
            numero = len(contas) + 1
            criar_nova_conta(numero, clientes, contas)
        elif opcao == "6":
            listar_todas(contas)
        elif opcao == "0":
            print("\n>>> Sistema encerrado. Até logo!")
            break
        else:
            print("\n!!! Opção inválida, tente novamente !!!")


# Inicia o programa
main()
