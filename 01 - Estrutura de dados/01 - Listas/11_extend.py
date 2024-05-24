# Método extend()
# O método extend() adiciona elementos de uma lista (ou qualquer iterável) ao final de outra lista.
# Sintaxe: nome_variavel.extend(<iterável>)
''' 
Diferente do método append(), O método extend() é utilizado para adicionar múltiplos elementos ao final de uma lista.
Ele recebe um iterável como argumento, como outra lista, 
e adiciona todos os elementos desse iterável à lista original.
'''


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(f'list1 antes: {list1}')  # [1, 2, 3, 4, 5]
list1.extend(list2)
print(f'list1 após extend: {list1}')  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

