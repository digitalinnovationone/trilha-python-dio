linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# O método index retorna o índice apenas da primeira ocorrência.
nomes = ["Ana", "Julio", "José", "Ana", "Pedro"]
print(nomes.index("Ana"))  # 0

# Caso o valor passado não esteja na lista ocorrerá um erro de execução.
# print(linguagens.index("Elixir"))
