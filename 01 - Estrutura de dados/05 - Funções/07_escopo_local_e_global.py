salario = 2000


def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"A lista alterada tem os valores: {lista_aux}")
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)