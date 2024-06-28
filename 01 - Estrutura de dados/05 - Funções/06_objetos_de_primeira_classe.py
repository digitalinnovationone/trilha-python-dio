def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplica(a, b):
    return a*2-1 + b+5+3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, multiplica)
