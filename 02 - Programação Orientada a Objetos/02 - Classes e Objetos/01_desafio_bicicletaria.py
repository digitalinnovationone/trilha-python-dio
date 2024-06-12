class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # self = referência explicita
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")
        
    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")
        
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else: 
                print("Não foi possível trocar de marcha...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#b1 = Bicicleta("vermelha", "caloi", 2022, 600)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)

b3 = Bicicleta("vermelho", "nike", 2010, 1500)
print(b2)
print(b3)
b2.correr()
