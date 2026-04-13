import textwrap


# ================== MODELOS ==================

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Valor inválido para depósito. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, usuario, limite=500, limite_saques=3):
        super().__init__(agencia, numero_conta, usuario)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente. @@@")

        elif valor > self.limite:
            print("\n@@@ Valor excede o limite. @@@")

        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Número máximo de saques excedido. @@@")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n@@@ Valor inválido para saque. @@@")


# ================== FUNÇÕES ==================

def menu():
    menu = """\n
    ================ MW BANK ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")

    if not cpf.isdigit():
        print("\n@@@ CPF inválido! Digite apenas números. @@@")
        return

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Nome completo: ")
    data = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")

    usuarios.append(Usuario(nome, data, cpf, endereco))
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = ContaCorrente(agencia, numero_conta, usuario)
        usuario.adicionar_conta(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta

    print("\n@@@ Usuário não encontrado! @@@")
    return None


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    for conta in contas:
        linha = f"""
        Agência:\t{conta.agencia}
        C/C:\t\t{conta.numero_conta}
        Titular:\t{conta.usuario.nome}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def selecionar_conta(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return None

    if not usuario.contas:
        print("\n@@@ Usuário não possui conta! @@@")
        return None

    if len(usuario.contas) == 1:
        return usuario.contas[0]

    print("\n=== Contas disponíveis ===")
    for indice, conta in enumerate(usuario.contas, start=1):
        print(
            f"{indice} - Agência: {conta.agencia} | "
            f"C/C: {conta.numero_conta} | "
            f"Titular: {conta.usuario.nome}"
        )

    try:
        opcao = int(input("Selecione o número da conta: "))
    except ValueError:
        print("\n@@@ Entrada inválida! Digite um número de conta válido. @@@")
        return None

    if 1 <= opcao <= len(usuario.contas):
        return usuario.contas[opcao - 1]

    print("\n@@@ Conta selecionada inválida! @@@")
    return None
# ================== MAIN ==================

def main():
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "1":
            conta = selecionar_conta(usuarios)
            if conta:
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)
                except ValueError:
                    print("\n@@@ Entrada inválida! Digite um número. @@@")

        elif opcao == "2":
            conta = selecionar_conta(usuarios)
            if conta:
                try:
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)
                except ValueError:
                    print("\n@@@ Entrada inválida! Digite um número. @@@")

        elif opcao == "3":
            conta = selecionar_conta(usuarios)
            if conta:
                conta.exibir_extrato()

        elif opcao == "7":
            print("\n=== Saindo do sistema... ===")
            break

        else:
            print("\n@@@ Opção inválida @@@")


if __name__ == "__main__":
    main()
