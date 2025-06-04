from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)    
  
    def adicionar_conta(self, conta):
        self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class PessoaJuridica(Cliente):
    def __init__(self, nome_empresa, cnpj, endereco):
        super().__init__(endereco)
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj

class Conta():
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
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
        return self.cliente
                        
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('Saldo insuficiente')
        elif valor > 0:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
            return True
        else:
            print('Não foi concluir a transação')
        
        return False
    
    def Depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            print('Depósito realizado!')
        else:
            print('Valor inválido')
            return False
        
        return True
    
class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if self.limite_saques <= 0:
            print("Limite de saques excedido!")
            return False

        if valor > self.saldo + self.limite:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor  # Usando o atributo protegido diretamente
        self.limite_saques -= 1
        print("Saque realizado com sucesso!")
        return True

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if self.limite_saques <= 0:
            print("Limite de saques excedido!")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        self.limite_saques -= 1
        print("Saque realizado com sucesso!")
        return True
    def Depositar(self, valor):
        return super().Depositar(valor) 
    
    def transferir(self, valor, conta_destino): 
        if valor <= 0:
            print("Valor inválido para transferência.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        conta_destino.Depositar(valor)
        print("Transferência realizada com sucesso!")
        return True
            
class Historico():  
    def __init__(self):
        self.transacoes = []
        
    def registrar(self, transacao):
        self.transacoes.append(transacao)
        print("Transação registrada com sucesso!")
    def listar(self):
        for transacao in self.transacoes:
            print(transacao)


