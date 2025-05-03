class veiculo:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        print("O veículo está se movendo")


class Carro(veiculo):
    def mover(self):
        print("O carro está se movendo")


class Aviao(veiculo):
    def mover(self):
        print("O Avião está se voando")


transportes = [Carro('Uno'), Aviao('ATR')]


for t in transportes:
    t.mover()