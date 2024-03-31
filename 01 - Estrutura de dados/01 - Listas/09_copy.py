lista1 = [1, "Python", [40, 30, 20]]
lista2 = lista1
lista3 = lista1.copy()

print("Conteúdo da lista original:")
print(lista1)  # [1, "Python", [40, 30, 20]]

print("Verificando igualidade com atribuição usando =")
print("Lista 1 is lista 2 ->", lista1 is lista2)

print("Verificando igualdade com atribuição usando copy")
print("Lista 1 is lista 3 ->", lista1 is lista3)

# As alterações na copia não afetam a lista original
lista3[0] = -1
print("Lista original:", lista1)
print("Lista copiada:", lista3)
