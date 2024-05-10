class Bicicleta: 
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('brim... brim... brim...')

    def parar(self):
        print('stop')

    def correr(self):
        print('runnn')
        

b1 = Bicicleta('vermelho', 'caloi', 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

