conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {2, 3, 5}
# Diferença entre dois conjuntos

resultado = conjunto_a.difference(conjunto_b, conjunto_c)
# Diferença entre três conjuntos
print(resultado)

resultado = conjunto_b.difference(conjunto_a, conjunto_c)
# Diferença entre três conjuntos
print(resultado)

resultado = conjunto_c.difference(conjunto_a, conjunto_b)
# Diferença entre três conjuntos
print(resultado)
