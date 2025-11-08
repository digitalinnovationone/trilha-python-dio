from sqlite3 import Cursor

from dominio import Cliente, PessoaFisica, PessoaJuridica


class ClienteServico:
    def __init__(self, cursor: Cursor) -> None:
        self.cursor = cursor

    def filtrar_cliente(self, documento: str) -> Cliente | None:
        pass

    def _criar_cliente_pessoa_fisica(self, documento: str) -> PessoaFisica:
        nome = input("Informe o nome completo: ")
        renda_mensal = float(input("Informe sua renda mensal: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        return PessoaFisica(
            nome=nome, cpf=documento, renda_mensal=renda_mensal, email=email, telefone=telefone, status="ativo"
        )

    def _criar_cliente_pessoa_juridica(self, documento: str) -> PessoaJuridica:
        nome = input("Informe o nome fantasia: ")
        faturamento_anual = float(input("Informe sua renda mensal: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        return PessoaJuridica(
            nome_fantasia=nome,
            cnpj=documento,
            faturamento_anual=faturamento_anual,
            email=email,
            telefone=telefone,
            status="ativo",
        )

    def criar_cliente(self) -> None:
        documento = input("Informe o documento (CPF/CNPJ): ")
        cliente = self.filtrar_cliente(documento)

        if cliente:
            print("\n@@@ Já existe cliente com esse documento (CPF/CNPJ)! @@@")
            return

        if len(documento) == 11:
            cliente = self._criar_cliente_pessoa_fisica(documento=documento)
        else:
            cliente = self._criar_cliente_pessoa_juridica(documento=documento)

        print(cliente)
        print("\n=== Cliente criado com sucesso! ===")

    def listar_clientes(self) -> None:
        print("Não existem clientes cadastrados!")
