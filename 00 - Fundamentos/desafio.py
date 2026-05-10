from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: 'Conta') -> None:
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self) -> float:
        return self.__valor

    def registrar(self, conta: 'Conta') -> None:
        sucesso = conta.depositar(self.__valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self) -> float:
        return self.__valor

    def registrar(self, conta: 'Conta') -> None:
        sucesso = conta.sacar(self.__valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self.__transacoes: list[Transacao] = []

    @property
    def transacoes(self) -> list[Transacao]:
        return self.__transacoes

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self.__transacoes.append(transacao)

    def gerar_extrato(self) -> str:
        linhas = []
        for t in self.__transacoes:
            tipo = 'Entrada' if isinstance(t, Deposito) else 'Saida'
            linhas.append(f'{tipo}: R$ {t.valor:.2f}')
        return '\n'.join(linhas)

class Conta:
    def __init__(self, cliente: 'Cliente', numero: int):
        self.__saldo: float = 0.0
        self.__numero: int = numero
        self.__agencia: str = '0001'
        self.__cliente: 'Cliente' = cliente
        self.__historico: Historico = Historico()

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def cliente(self) -> 'Cliente':
        return self.__cliente

    @property
    def historico(self) -> Historico:
        return self.__historico

    @classmethod
    def nova_conta(cls, cliente: 'Cliente', numero: int) -> 'Conta':
        return cls(cliente, numero)

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print('Operacao invalida. O valor informado e invalido.')
            return False
        self.__saldo += valor
        print(f'Deposito de R$ {valor:.2f} realizado com sucesso.')
        return True

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print('Operacao invalida. O valor informado e invalido.')
            return False
        if valor > self.__saldo:
            print('Operacao invalida. Saldo insuficiente.')
            return False
        self.__saldo -= valor
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente: 'Cliente', numero: int,
                 limite: float = 500.0, limite_saques: int = 3):
        super().__init__(cliente, numero)
        self.__limite: float = limite
        self.__limite_saques: int = limite_saques

    @classmethod
    def nova_conta(cls, cliente: 'Cliente', numero: int,  # type: ignore[override]
                   limite: float = 500.0, limite_saques: int = 3) -> 'ContaCorrente':
        return cls(cliente, numero, limite, limite_saques)

    def sacar(self, valor: float) -> bool:
        numero_saques_realizados = sum(
            1 for t in self.historico.transacoes if isinstance(t, Saque)
        )

        if valor <= 0:
            print('Operacao invalida. O valor informado e invalido.')
            return False
        if valor > self.saldo:
            print('Operacao invalida. Saldo insuficiente.')
            return False
        if valor > self.__limite:
            print(f'Operacao invalida. Valor excede o limite de R$ {self.__limite:.2f} por saque.')
            return False
        if numero_saques_realizados >= self.__limite_saques:
            print('Operacao invalida. Numero maximo de saques diarios atingido.')
            return False

        return super().sacar(valor)

    def __str__(self) -> str:
        return (
            f'Agencia:\t{self.agencia}\n'
            f'Conta:\t\t{self.numero}\n'
            f'Titular:\t{self.cliente.nome}'
        )

class Cliente:
    def __init__(self, endereco: str):
        self.__endereco: str = endereco
        self.__contas: list[Conta] = []

    @property
    def endereco(self) -> str:
        return self.__endereco

    @property
    def contas(self) -> list[Conta]:
        return self.__contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta) -> None:
        self.__contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, endereco: str):
        super().__init__(endereco)
        self.__cpf: str = cpf
        self.__nome: str = nome
        self.__data_nascimento: str = data_nascimento

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento


def filtrar_cliente(cpf: str, clientes: list[PessoaFisica]):
    resultado = [c for c in clientes if c.cpf == cpf]
    return resultado[0] if resultado else None


def recuperar_conta_cliente(cliente: Cliente) -> Conta | None:
    if not cliente.contas:
        print('Erro... Cliente nao possui conta cadastrada.')
        return None
    # Se tiver apenas uma conta, usa ela diretamente;
    # caso contrário, permite escolher.
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    print('Contas disponíveis:')
    for i, c in enumerate(cliente.contas, 1):
        print(f'  {i} - Ag: {c.agencia} | Conta: {c.numero}')
    try:
        idx = int(input('Escolha o numero da conta: ')) - 1
        return cliente.contas[idx]
    except (ValueError, IndexError):
        print('Selecao invalida.')
        return None


def depositar(clientes: list[PessoaFisica]) -> None:
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('Erro... Cliente nao encontrado.')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input('Valor do deposito: R$ '))
    except ValueError:
        print('Erro... Digite apenas numeros.')
        return

    cliente.realizar_transacao(conta, Deposito(valor))


def sacar(clientes: list[PessoaFisica]) -> None:
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('Erro... Cliente nao encontrado.')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input('Valor do saque: R$ '))
    except ValueError:
        print('Erro... Digite apenas numeros.')
        return

    cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(clientes: list[PessoaFisica]) -> None:
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('Erro... Cliente nao encontrado.')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print('\n--- Extrato ---')
    extrato = conta.historico.gerar_extrato()
    print('Nao foram realizadas movimentacoes.' if not extrato else extrato)
    print(f'Saldo atual: R$ {conta.saldo:.2f}')
    print('----------------')


def criar_cliente(clientes: list[PessoaFisica]) -> None:
    cpf = input('CPF (somente numeros): ')

    if len(cpf) != 11 or not cpf.isdigit():
        print('Erro... CPF invalido. Digite exatamente 11 digitos numericos.')
        return

    if filtrar_cliente(cpf, clientes):
        print('Erro... Ja existe um cliente com esse CPF.')
        return

    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    logradouro = input('Logradouro: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    sigla_estado = input('Sigla do estado (ex: SP, RJ): ').upper()

    endereco = f'{logradouro} - {bairro} - {cidade}/{sigla_estado}'

    cliente = PessoaFisica(
        cpf=cpf,
        nome=nome,
        data_nascimento=data_nascimento,
        endereco=endereco,
    )
    clientes.append(cliente)
    print(f'Cliente {nome} cadastrado com sucesso!')


def criar_conta(numero_conta: int, clientes: list[PessoaFisica],
                contas: list[ContaCorrente]) -> None:
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('Erro... Cliente nao encontrado. Cadastre o cliente antes de criar uma conta.')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f'Conta corrente criada com sucesso!\n{conta}')


def listar_contas(contas: list[ContaCorrente]) -> None:
    if not contas:
        print('Nenhuma conta cadastrada.')
        return
    for conta in contas:
        print('=' * 30)
        print(conta)
    print('=' * 30)
    

def sistema_bancario() -> None:
    clientes: list[PessoaFisica] = []
    contas: list[ContaCorrente] = []

    menu_opcoes = [
        'Depositar',
        'Sacar',
        'Extrato',
        'Novo Cliente',
        'Nova Conta',
        'Listar Contas',
        'Sair',
    ]

    while True:
        print('-' * 30)
        print('    Sistema Bancario')
        print('-' * 30)
        for i, opcao in enumerate(menu_opcoes, start=1):
            print(f'  {i} - {opcao}')
        print('-' * 30)

        try:
            escolha = int(input('Escolha uma opcao: '))
        except ValueError:
            print('Erro... Digite apenas numeros.')
            continue

        if escolha == 1:
            depositar(clientes)
        elif escolha == 2:
            sacar(clientes)
        elif escolha == 3:
            exibir_extrato(clientes)
        elif escolha == 4:
            criar_cliente(clientes)
        elif escolha == 5:
            criar_conta(len(contas) + 1, clientes, contas)
        elif escolha == 6:
            listar_contas(contas)
        elif escolha == 7:
            print('Saindo do sistema. Ate logo!')
            break
        else:
            print('Opcao invalida. Tente novamente.')


if __name__ == '__main__':
    sistema_bancario()