menu = """
============ Banco Py ===========

Bem vindo os sistema do Banco Py

=================================
"""

def novaConta(agencia, conta, senha, nome):
    return {
        "agencia": "",
        "conta": "",
        "senha": "",
        "nome": ""
    }


print(" Entre com os dados da sua Agência e conta. \n Não incluia traços e/ou pontos, apenas numeros. ")

while True:
    agencia = input("Agência: ")
    if len(agencia) != 4:
        print("Sua agencia deve contar 4 digitos numéricos. \n Digite novamente")
        agencia = input("Agência: ")

    
        