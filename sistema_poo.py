from datetime import date
from abc import ABC, abstractclassmethod, abstractproperty

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self) -> float:
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
    
    @classmethod
    def nova_conta(cls, cliente, numero: int) -> "Conta":
        return cls(cliente, numero)
    
    def sacar(self, valor: float):
        excedeu_saldo = valor > self._saldo

        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado!")
            return True 
        
        elif excedeu_saldo:
            print("Saldo Insuficiente!")
            return True
        
        else: 
            print("A operação falhou!")
        return False
     
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado!")
            
        else:
            print("Valor inválido!")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        excedeu_saques = self.saques_realizados >= self.limite_saques
        excedeu_saldo = valor > self._saldo

        if excedeu_saques:
            print("Limite de saque excedido!")
        
        elif excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif valor > 0:
            self._saldo -= valor
            self.saques_realizados += 1
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou!")

        return False
        
class Historico:

    
    def __init__ (self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor
                "data": datetime.now().strftime
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

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
       
class Saque(Transacao):
    def __init__(self, conta, tipo, valor: float):
        super().__init__(conta, tipo, valor)
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
