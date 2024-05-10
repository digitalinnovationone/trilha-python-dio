from abc import ABC, abstractclassmethod, abstractmethod

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._agencia = '0001' #definida por padrão
        self._cliente = cliente
        self._saldo = 0 #inicial da conta
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n === Depósito realizado ===')
        else: 
            print('\n === ERRO NA OPERAÇÃO ===')
            return False
        
        return True
    
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realiza_transacao(self, conta, transacao):
        transacao.registra(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class ContaCorrente:
    def __init__(self, limite, limite_saque):
        self.limite = limite
        self.limite_saque = limite_saque


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registra(self, conta):
        pass

class Historico:
    def __init__(self):
        self._transcao = []

    def adiciona_transacao(self, transacao):
        self._transcao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sussesso_transacao = conta.depositar(self.valor)

        if sussesso_transacao:
            conta.historico.adicionar_transição(self)

class Saque:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor



fcliente = Cliente('rua testes - bairro, cidade tal')
fconta = Conta(1212, fcliente);

fconta.depositar(200)

print(fconta.cliente)