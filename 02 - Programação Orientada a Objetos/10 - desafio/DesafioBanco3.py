import textwrap
from typing import Iterator
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
class Lista():
    def __init__(self):
        self.registros = {}
    def __setitem__(self, chave, valor):
        self.registros[chave] = valor

class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        Pessoas._regs_cls[self.cpf] = self
    def __str__(self):
        return f"""\
            Nome:\t{self.nome}
            CPF:\t{self.cpf}
            Data de nacimento:\t{self.data_nascimento}
            Endereço:\t{self.endereco}
        """
    
class Cliente(Pessoa):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.contas = Contas()
        Clientes._regs_cls[self.cpf] = self
    def criar_conta(self, senha) -> 'Conta':
        conta = Conta(self, senha)
        self.contas.adicionar(conta)
        print(f"=== Conta de número {conta.codigo} criada com sucesso! ===")
        return conta
    def criar_contabasica(self, senha, limite=500, limite_saques=3) -> 'ContaBasica':
        conta = ContaBasica(self, senha, limite=500, limite_saques=3)
        self.contas.adicionar(conta)
        print(f"=== Conta de número {conta.codigo} criada com sucesso! ===")
        return conta
    
class Pessoas(Lista):
    _regs_cls = {}
    def __init__(self):
        super().__init__()
        self.clientes = Clientes()
    def adicionar(self, pessoa: Pessoa):
        if isinstance(pessoa, Cliente):
            self.clientes[pessoa.cpf] = pessoa
        self.registros[pessoa.cpf] = pessoa
        print(f"=== {pessoa.nome} cadastrado com sucesso! ===")
    def __getitem__(self, cpf) -> Pessoa:
        return self.registros[cpf]
    def __iter__(self) -> Iterator[Pessoa]:
        return iter(self.registros.values())
    @staticmethod
    def index(cpf) -> Pessoa:
        return Pessoas._regs_cls[cpf]
    
class Clientes(Lista):
    _regs_cls = {}
    def adicionar(self, cliente: Cliente):
        self.registros[cliente.cpf] = cliente
        print(f"=== Cliente de número {cliente.cpf} criada com sucesso! ===")
    def __getitem__(self, cpf) -> Cliente: # Para obter a posição do objeto na lista: def Index(self, cpf) -> Cliente: 
        return self.registros[cpf]              # return self.registros[list(self.registros.keys())[cpf]]
    def __iter__(self) -> Iterator[Cliente]:
        return iter(self.registros.values())
    @staticmethod
    def index(cpf) -> Cliente:
        return Clientes._regs_cls[cpf]
    
class Conta: 
    def __init__(self, cliente: Cliente, senha):
        self.senha = senha
        self._saldo = 0
        self._codigo = len(Contas._regs_cls)
        self._agencia = "0001"
        self._cliente = cliente
        self._transacoes = Transacoes()
        Contas._regs_cls[self._codigo] = self
    @property
    def saldo(self):
        return self._saldo
    @property
    def codigo(self):
        return self._codigo
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    @property
    def transacoes(self) -> 'Transacoes':
        return self._transacoes
    def sacar(self, valor=0) -> bool:
        valor = float(input("Informe o valor do depósito: ")) if valor == 0 else valor
        saldo = self.saldo
        if valor > saldo:
            print("@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            saque = Saque(self, valor)
            self._transacoes.adicionar(saque)
            self._saldo -= valor
            print("=== Saque realizado com sucesso! ===")
            return True
        else:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")
        return False
    def depositar(self, valor=0) -> bool:
        valor = float(input("Informe o valor do depósito: ")) if valor == 0 else valor
        if valor > 0:
            deposito = Deposito(self, valor) # Acrescentar self para associar a conta ao deposito
            self._transacoes.adicionar(deposito)
            self._saldo += valor
            print("=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
    def exibir_extrato(self):
        print(f"================ Extrato Conta: {self.codigo} ================")
        transacoes = self.transacoes
        extrato = ""
        if not transacoes.registros:
            extrato = "Não foram realizadas movimentações."
        else:
            for transacao in transacoes:
                extrato += f"{transacao.tipo} ({transacao.data}):\n\tR$ {transacao.valor:.2f}\n"
        print(extrato)
        print(f"Saldo:\n\tR$ {self.saldo:.2f}")
        print("==========================================")
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta:\t{self.codigo}
            Titular:\t{self.cliente.nome}
        """

class ContaBasica(Conta):
    def __init__(self, cliente: Cliente, senha, limite=500, limite_saques=3):
        super().__init__(cliente, senha)
        self._limite = limite
        self._limite_saques = limite_saques
        ContasBasicas._regs_cls[self.codigo] = self
    def sacar(self, valor=0):
        numero_saques = len( # for id_usuario, dados_usuario in usuarios.items():
            [transacao for transacao in self.transacoes if transacao.tipo == Saque.__name__]) # .registros
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
        if excedeu_limite:
            print("@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)
        return False

class Contas(Lista):
    _regs_cls = {}
    def __init__(self):
        super().__init__()
        self.contasbasicas = ContasBasicas()
    def adicionar(self, conta: Conta):
        if isinstance(conta, ContaBasica):
            self.contasbasicas[conta.codigo] = conta
        self.registros[conta.codigo] = conta
    def __getitem__(self, codigo) -> Conta:
        return self.registros[codigo]
    def __iter__(self) -> Iterator[Conta]:
        return iter(self.registros.values())
    @staticmethod
    def index(codigo) -> 'Conta':
        return Contas._regs_cls[codigo]

class ContasBasicas(Lista):
    _regs_cls = {}
    def adicionar(self, ContaPremium: ContaBasica):
        self.registros[ContaPremium.codigo] = ContaPremium
        print(f"=== Conta de número {ContaPremium.codigo} criada com sucesso! ===")
    def __getitem__(self, codigo) -> ContaBasica:
        return self.registros[codigo]
    def __iter__(self) -> Iterator[ContaBasica]:
        return iter(self.registros.values())
    @staticmethod
    def index(codigo) -> ContaBasica:
        return ContasBasicas._regs_cls[codigo]
    
class Transacao(ABC):
    def __init__(self, conta: Conta): #, conta: Conta
        self._conta = conta
        self._codigo = len(Transacoes._regs_cls)
        self._tipo = self.__class__.__name__
        self._data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        Transacoes._regs_cls[self._codigo] = self
    @property
    def conta(self):
        return self._conta
    @property
    def codigo(self):
        return self._codigo
    @property
    def tipo(self):
        return self._tipo
    @property
    def data(self):
        return self._data
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta: Conta):
        pass

class Saque(Transacao):
    def __init__(self, conta: Conta, valor):
        super().__init__(conta)
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta:Conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.transacoes.adicionar(self)

class Deposito(Transacao):
    def __init__(self, conta: Conta, valor):
        super().__init__(conta)
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta:Conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.transacoes.adicionar(self)
            
class Transacoes(Lista):
    _regs_cls = {}
    def adicionar(self, transacao: Transacao):
        self.registros[transacao.codigo] = transacao
    def __getitem__(self, codigo) -> Transacao:
        return self.registros[codigo]
    def __iter__(self) -> Iterator[Transacao]:
        return iter(self.registros.values())
    @staticmethod
    def index(codigo) -> Transacao:
        return Contas._regs_cls[codigo]
    
class Interface():
    def __init__(self, pessoas: Pessoas, contas: Contas):
        while True:
            resposta = self.menu()
            if resposta == "lo": #Login
                codigo = int(input("Informe o código da conta: "))
                conta = contas[codigo]
                if conta:
                    senha = input("Informe a senha da conta: ")
                    if senha == conta.senha:
                        while True:
                            resposta = self.menulogin()
                            if resposta == "d":
                                conta.depositar()
                            elif resposta == "s":
                                conta.sacar()
                            elif resposta == "e":
                                conta.exibir_extrato()
                            elif resposta == "q":
                                break
                            else:
                                print("Operação inválida, por favor selecione novamente a operação desejada.")
                    else:
                        print("\n@@@ Senha inválida, por favor selecione novamente a operação desejada. @@@")
                else:
                    print("\n@@@ Conta não existe! @@@")
            elif resposta == "nu": #Criar_usuário
                cpf = input("Informe o CPF (somente número): ")
                try:
                    cliente = pessoas[cpf]
                    print(f"\n@@@ {cliente.nome} está cadastrado com esse CPF! @@@")
                    continue
                except:
                    nome = input("Informe o nome completo: ")
                    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
                    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
                    pessoas.adicionar(Cliente(cpf, nome, data_nascimento, endereco))
            elif resposta == "lu": #Listar_usuarios
                for pessoa in pessoas:
                    print(pessoa.__class__.__name__)
                    print(pessoa)
            elif resposta == "nc": #Criar_conta
                cpf = input("Informe o CPF (somente número): ")
                try:
                    cliente = pessoas.clientes[cpf]
                    senha = input("Informe a senha: ")
                    conta = cliente.criar_contabasica(senha)
                    contas.adicionar(conta)
                    continue
                except:
                    print(f"\n@@@ CPF não cadastrado, cadastre-se! @@@")
            elif resposta == "lc": #Listar_contas
                for conta in contas:
                    print(conta.__class__.__name__)
                    print(conta)
            elif resposta == "q": #Sair
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
    def menu(self):
        menu = """\n
        ================ MENU ================
        [lo]\tFazer login
        [nu]\tNovo usuário
        [nc]\tNova conta

        [lu]\tLista usuário
        [lc]\tLista contas

        [q]\tSair
        => """
        return input(textwrap.dedent(menu))    
    def menulogin(self):
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato

        [q]\tSair
        => """
        return input(textwrap.dedent(menu))
##############################################################################################################################################################################
pessoas = Pessoas()
pessoas.adicionar(Pessoa(cpf='0', nome='Nome 0', data_nascimento='01/01/1990', endereco='end1'))
pessoas.adicionar(Pessoa(cpf='1', nome='Nome 1', data_nascimento='01/01/1990', endereco='end1'))
pessoas.adicionar(Cliente(cpf='2', nome='Nome 2', data_nascimento='01/01/1990', endereco='end1'))
pessoas.adicionar(Cliente(cpf='3', nome='Nome 3', data_nascimento='01/01/1990', endereco='end1'))
pessoas.adicionar(Pessoa(cpf='4', nome='Nome 4', data_nascimento='01/01/1990', endereco='end1'))
pessoas.adicionar(Cliente(cpf='5', nome='Nome 5', data_nascimento='01/01/1990', endereco='end1'))
contas = Contas()
contas.adicionar(pessoas.clientes['3'].criar_conta(senha='abc'))
contas.adicionar(pessoas.clientes['2'].criar_contabasica(senha='abc'))
pessoas.clientes['2'].contas[1].depositar(1000)
pessoas.clientes['2'].contas[1].sacar(150)
pessoas.clientes['2'].contas[1].sacar(150)
pessoas.clientes['2'].contas[1].sacar(150)
pessoas.clientes['2'].contas[1].sacar(150)
pessoas.clientes['2'].contas[1].exibir_extrato()
pessoas.clientes['3'].contas[0].depositar(1000)
pessoas.clientes['3'].contas[0].sacar(150)
pessoas.clientes['3'].contas[0].sacar(150)
pessoas.clientes['3'].contas[0].sacar(150)
pessoas.clientes['3'].contas[0].sacar(150)
pessoas.clientes['3'].contas[0].exibir_extrato()
print(f'contas[\'0\'].saldo: {Contas.index(0).saldo}') # Porque não poderia ser: "Contas[0].saldo" ?
print(f'contas[\'1\'].saldo: {Contas.index(1).saldo}')
print(f'\n\n\n\n')
interface = Interface(pessoas,contas)
