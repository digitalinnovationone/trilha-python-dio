class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade
    @classmethod   
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

#p = Pessoa("Luis", 46)

#print(p.nome, p.idade)
p = Pessoa.criar_de_data_nascimento(1978, 3, 22, "Luis")
print(p.nome, p.idade)