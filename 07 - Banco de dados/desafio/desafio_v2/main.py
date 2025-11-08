import sqlite3
import textwrap

from bd import criar_bd, criar_conexao
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
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.row_factory = sqlite3.Row

    criar_bd(cursor=cursor)

    servico = ClienteServico(cursor=cursor)

    while True:
        match menu():
            case "1":
                servico.criar_cliente()
                conexao.commit()
            case "2":
                servico.listar_clientes()
            case "0":
                break
            case _:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

    conexao.close()


main()
