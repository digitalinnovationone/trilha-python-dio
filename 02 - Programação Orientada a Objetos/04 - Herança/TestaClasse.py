# from Pessoa import *

# p = Pessoa("Ney", 32)
# p.aniversario()
# p.aniversario()
# p.aniversario()

# from Atleta import *
# a = Atleta("Bolt", 37, 94.0)
# a.aniversario()
# a.aquecer()
# print(f"Nome: {a.nome} | Idade: {a.idade} | Peso: {a.peso} kg")

from Corredor import *
from Nadador import *
from Ciclista import *

corredor = Corredor("Usain Bolt", 37, 1.95, 94)
print(f"Nome: {corredor.nome} | Idade: {corredor.idade} | Altura: {corredor.altura}m | Peso: {corredor.peso} kg")
corredor.aniversario()
corredor.aquecer()
corredor.correr()
print("\n================================\n")

nadador = Nadador("Michael Phelps", 38, 1.93, 88)
print(f"Nome: {nadador.nome} | Idade: {nadador.idade} | Altura: {nadador.altura}m | Peso: {nadador.peso} kg")
nadador.aniversario()
nadador.aquecer()
nadador.nadar()
print("\n================================\n")

ciclista = Ciclista("Lance Armstrong", 52, 1.77, 75)
print(f"Nome: {ciclista.nome} | Idade: {ciclista.idade} | Altura: {ciclista.altura}m | Peso: {ciclista.peso} kg")
ciclista.aniversario()
ciclista.aquecer()
ciclista.pedalar()


