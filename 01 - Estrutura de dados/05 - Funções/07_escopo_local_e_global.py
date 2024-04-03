salario = 2000


def salario_bonus(bonus, lista):
    global salario
    salario += bonus
    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f"Lista Auxiliar: {lista_auxiliar}")
    return salario


lista = [1]
print(salario_bonus(500, lista))  # 2500
print(f"Lista Original: {lista}")
