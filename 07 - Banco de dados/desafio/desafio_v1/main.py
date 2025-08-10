import textwrap

from servico import ClienteServico


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tNovo cliente
    [2]\tListar clientes
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    servico = ClienteServico(cursor=None)

    while True:
        match menu():
            case "1":
                servico.criar_cliente()
            case "2":
                servico.listar_clientes()
            case "0":
                break
            case _:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
