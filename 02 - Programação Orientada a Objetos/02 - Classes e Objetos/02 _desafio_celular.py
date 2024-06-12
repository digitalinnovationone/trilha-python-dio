from datetime import date
import datetime as dt

class Celular:
    def __init__(self, ano, modelo, cor, valor):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
    
    def atualiza_valor(self, valor):
        novo_valor = valor
        self.valor = novo_valor
        


cel1 = Celular("2015", "Galaxy S5", "Branco", 5000)

cel1.atualiza_valor(10000)

print(cel1.valor)

print(date.today())

print(dt.datetime.now()) 
