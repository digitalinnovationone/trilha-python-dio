linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# Caso haja o mesmo valor na duas listas esse valor será duplicado
# na lista resultante.

linguagens.extend(["java", "ruby", "php"])
print(linguagens)
