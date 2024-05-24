# Método sort()
# O método sort() ordena os elementos de uma lista.
# Sintaxe: nome_variavel.sort()

# Exemplo 1
numero = [10, 2, 8, 5, 4, 6, 7, 3, 9, 1]
print('Lista Original: \n',numero) # [10, 2, 8, 5, 4, 6, 7, 3, 9, 1]

numero.sort()

print('Lista Ordenada: \n',numero)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('')

# O método sort() também aceita os argumentos reverse e key.
# O argumento reverse é um booleano que indica se a lista deve ser ordenada em ordem decrescente.
# O argumento key é uma função que define a chave de ordenação.

# Exemplo 2
print('')
numero = [10, 2, 8, 5, 4, 6, 7, 3, 9, 1]
print('Lista Original: \n',numero)  # [10, 2, 8, 5, 4, 6, 7, 3, 9, 1]
numero.sort(reverse=True)
print('Lista Ordenada em Ordem Decrescente: \n',numero)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  
print('')

# Exemplo 3
numero = [1,2,3,4,5,6,7,8,9,10]
print('Lista Original: \n',numero)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero.sort(key=lambda x: x % 2)
print('Lista Ordenada por Paridade: \n',numero)  # [2, 4, 6, 8, 10, 1, 3, 5, 7, 9] 
print('')

# Exemplo 4
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)
print('')


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)
print('')

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)
print('')

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
print('')