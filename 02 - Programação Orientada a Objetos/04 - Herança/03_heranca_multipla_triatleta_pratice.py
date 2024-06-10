class Pessoa:
    def __init__(self, nome=str, idade=int):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def aniversario(self):
        self.idade += 1
        print("%s, parabéns pelos seus %d anos de idade." %(self.nome, self.idade))

class Atleta(Pessoa):
    def __init__(self, peso=int, **kw):
        
        super().__init__(**kw)
        self.peso = peso

class Corredor(Atleta):
    def __init__(self, nome, idade, peso):
        super().__init__(nome=nome, idade=idade, peso=peso)

    def correr(self):
        print("correndo..")

class Nadador(Atleta):
    def __init__(self, **kw):
        super().__init__(**kw)

    def nadar():
        pass

class Ciclista(Atleta):
    def __init__(self, **kw):
        super().__init__(**kw)

    def pedalar():
        pass

p1 = Corredor("Bolt", 35, 40)
print(p1)
p1.correr()