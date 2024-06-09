class Livro:
    def __init__(self, nome, preco, autor, numero_paginas, capa_comum=True):
        self.nome = nome
        self.preco = preco
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.capa_comum = capa_comum
    
    def lendo(self):
        print("Estou lendo")

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])})"

class Livro_1(Livro):
    def __init__(self, nome, preco, autor, numero_paginas, lido):
        super().__init__(nome, preco, autor, numero_paginas)
        self.lido = lido
    
    def ja_li(self):
         print(f"{'Sim já' if self.lido else 'Não'} li!")

class Livro_2(Livro):
    def __init__(self, nome, preco, autor, numero_paginas, lido):
        super().__init__(nome, preco, autor, numero_paginas)
        self.lido = lido
    
    def ja_li(self):
         print(f"{'Sim já' if self.lido else 'Não'} li!")


class Livro_3(Livro):
    def __init__(self, nome, preco, autor, numero_paginas, lido):
        super().__init__(nome, preco, autor, numero_paginas)
        self.lido = lido
    
    def ja_li(self):
         print(f"{'Sim já' if self.lido else 'Não'} li!")

a = Livro_1("Mais esperto que o Diabo", "29,90", "Napoleon Hill", 208, False)

b = Livro_2("Como convencer alguém em 90 segundos", "37,40", "Nicholas Boothman", 264, False)

c = Livro_3("33 estratégias de guerra", "38,70", "Robert Greene", 216, False)

print(a)
a.ja_li()

print(b)
b.ja_li()

print(c)
c.ja_li()