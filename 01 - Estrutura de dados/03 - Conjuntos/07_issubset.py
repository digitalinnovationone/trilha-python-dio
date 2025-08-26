conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_c = {1, 2, 3, 4, 5}
# Verifica se um conjunto é subconjunto de outro

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

resultado = conjunto_c.issubset(conjunto_a)  # False
print(resultado)

resultado = conjunto_a.issubset(conjunto_c)  # True
print(resultado)

