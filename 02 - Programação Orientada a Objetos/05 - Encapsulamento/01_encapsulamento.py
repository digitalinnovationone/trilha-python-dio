class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.__saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self.__saldo += valor

    def sacar(self, valor):
        # ...
        self.__saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self.__saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
