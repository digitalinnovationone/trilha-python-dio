class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def idade(self):
        __ano_atual = 2022
        return __ano_atual - self.__ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
