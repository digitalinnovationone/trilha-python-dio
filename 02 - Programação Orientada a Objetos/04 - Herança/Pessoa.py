class Pessoa:
    def __init__(self, nome=str, idade=int):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        print("%s, parabéns pelos seus %d anos de idade." %(self.nome, self.idade))