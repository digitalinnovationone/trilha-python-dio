from Pessoa import *

class Atleta(Pessoa): 
    def __init__(self, nome=str, idade=int, altura=int, peso=int): 
        super(Atleta, self).__init__(nome, idade)
        self.altura = altura
        self.peso = peso
    
    def aquecer(self):
        print("%s está aquecendo.." %self.nome)