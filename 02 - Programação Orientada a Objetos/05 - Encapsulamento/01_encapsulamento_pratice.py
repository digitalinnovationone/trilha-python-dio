class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ... simulando verificações
        self._saldo += valor

    def sacar(self, valor):
        # ... simulando verificações
        self._saldo -= valor

    def mostrar_saldo(self):
        # ... simulando verificações
        return self._saldo

conta = Conta("0001", 100)
#conta._saldo += 100 funciona, mas errado
conta.depositar(100)
print(conta.nro_agencia)
#print(conta._saldo) funciona, mas errado
print(conta.mostrar_saldo())