class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Começa o jogo...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância do jogo.")

    def mijar_em_filho_da_puta(self):
        print("Mijando em curintianus")

def criar_gênio():
    dog = Cachorro("Calleri", "Tricolor!!!")
    print(dog.nome, dog.cor)

    dog.mijar_em_filho_da_puta()

criar_gênio()