class Cliente:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"


class ContaBancaria:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.limite = 500.0
        self.extrato = []
        self.numero_saques = 0
        self.limite_saques = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("Saque realizado.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if self.extrato:
            print("\n".join(self.extrato))
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


def criar_usuario(usuarios):
    nome = input("Digite o seu nome: ")
    nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o seu CPF: ")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Esse CPF já está cadastrado.")
            return None

    print("\n============= ENDEREÇO =============")
    rua = input("Rua: ")
    bairro = input("Bairro: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco = f"{rua}, {bairro}, {numero} - {cidade}/{estado}"

    novo_usuario = Cliente(nome, nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            conta = ContaBancaria(agencia, numero, usuario)
            print("Conta criada com sucesso!")
            return conta

    print("Usuário não encontrado. Conta não criada.")
    return None


def principal():
    usuarios = []
    contas = []
    numero_conta = 1
    agencia_padrao = "0001"

    while True:
        opcao = input("""
=========== MENU ===========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Sair
=> """)

        if opcao == "1":
            cpf = input("Informe o CPF do titular: ")
            conta = next((c for c in contas if c.cliente.cpf == cpf), None)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "2":
            cpf = input("Informe o CPF do titular: ")
            conta = next((c for c in contas if c.cliente.cpf == cpf), None)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            cpf = input("Informe o CPF do titular: ")
            conta = next((c for c in contas if c.cliente.cpf == cpf), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = criar_conta(agencia_padrao, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            print("Obrigado por usar o banco. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")
