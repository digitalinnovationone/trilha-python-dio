#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
#Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!
#pode ser self ou outro nome como this. por exemplo, ele serve para criar um objeto a partir da classe(atributos da classe).
class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

b1= Bicicleta("vermelha", "caloi", 2020, 1500)
