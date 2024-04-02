def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


def media(values):
    return somar_valores(values) / len(values)


def somar_valores(values):
    soma = 0
    for value in values:
        soma += value
    return soma


exibir_resultado(12.34, 1.1415, somar)  # O resultado da operação 10 + 10 = 20
print(media([10, 9.5]))
