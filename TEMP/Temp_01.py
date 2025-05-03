class ContaBancaria:
    def __init__(self, nome_titular, saldo=0, operacoes=[]):
        self.nome_titular = nome_titular
        self.__saldo = saldo
        self.__operacoes = operacoes
    
    def depositar(self, valor):
        self.__saldo += valor
        self.__operacoes.append('+' + str(valor))

    def sacar(self, saque):
        if abs(saque) > self.__saldo:
            self.__operacoes.append('Saque não permitido')
        else:
            self.__saldo -= abs(saque)
            self.__operacoes.append(str(saque))
        

    def extrato(self):
        return print(f"Operações: {', '.join(self.__operacoes)}" + f"; Saldo: {self.__saldo}")
                    
transacoes = '100, -50, 200, -300'
transacoes_int = [int(valor) for valor in transacoes.split(",")]  

conta = ContaBancaria('Tysson')

for valor in transacoes_int:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)

conta.extrato()
from abc import ABC, abstractmethod

class Veiculo(ABC):  # ABC = Abstract Base Class
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está andando...")

class Aviao(Veiculo):
    def mover(self):
        print("O avião está voando...")

transportes = [Carro(), Aviao()]
for t in transportes:
    t.mover()
