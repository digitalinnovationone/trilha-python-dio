# Método sorted()
# A função sorted() em Python é usada para retornar uma nova lista ordenada a partir de um iterável (como listas, tuplas, conjuntos, etc.), deixando o iterável original inalterado. Ela pode ordenar os elementos em ordem crescente ou decrescente e pode ser personalizada com uma função de chave.
# Sintaxe: sorted(iterable, key=None, reverse=False)

numbers = [4, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Saída: [1, 2, 4, 5, 6, 9]

# Ordenando com reverse=True
numbers = [4, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Saída: [9, 6, 5, 4, 2, 1]

#Ordenando com uma função de chave
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Saída: ['apple', 'banana', 'cherry']


linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"] 
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
