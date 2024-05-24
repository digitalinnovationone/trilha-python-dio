# Title: Método copy()
# Descrição: O método copy() retorna uma cópia da lista
# Neste exemplo, a lista é copiada e exibida antes e depois da cópia
# Utilidade: Utilizado para copiar uma lista para outra variável sem alterar a original ou para criar uma cópia de segurança

# exemplo 1

numeros = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = numeros.copy()
print(num2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      
