class ContaBancaria:
    def __init__(self, titular=None, saldo=None):
        self.titular = titular
        self.saldo = saldo

class criando_conta(ContaBancaria):
    def criar_conta(self, titular, saldo, contas=dict()):
        self.titular = titular
        self.saldo = saldo
        self.contas = contas
        contas[self.titular] = self.saldo

    def listar_contas(self):
        return print(", ".join([f"{chave}: R$ {valor}" for chave, valor in self.contas.items()]))


# transacoes = 'Tysson, 50'
# transacoes_2 = transacoes.split(",")

# contas = dict()
# contas[transacoes_2[0]] = int(transacoes_2[1])
# print(contas.values())

sistema = criando_conta()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()