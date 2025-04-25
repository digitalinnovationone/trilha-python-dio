menu = """
============ SISTEMA BANCARIO ============

\033[1;36m[1] Registrar Usuario
[2] Cadastrar Conta
[3] Ver Usuarios Cadastrados
[4] Ver Contas Cadastradas
>>>>[5] Deposito
>>>>[6] Saque
>>>>[7] Extrato
[8] Sair\033[0m
Digite a opção desejada: """

# Classe Conta Bancaria
class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.limite = 500.0
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUE = 3

    def deposito_fun(self):
        try:
            deposito = float(input("Digite a quantidade de dinheiro que gostaria de depositar: R$ "))
            if deposito > 0:
                self.saldo += deposito
                self.extrato.append(f"\033[32mDepósito: R$ {deposito:.2f}\033[0m")
                print(f"Depósito realizado com sucesso! \033[34mSaldo atual: R$ {self.saldo:.2f}\033[0m")
            else:
                print("O valor do depósito deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    def saque_fun(self):
        try:
            saque = float(input("Digite a quantidade de dinheiro que gostaria de sacar: R$ "))
            if 0 < saque <= self.saldo and self.numero_saques < self.LIMITE_SAQUE and saque <= self.limite:
                self.saldo -= saque
                self.numero_saques += 1
                self.extrato.append(f"\033[31mSaque: R$ {saque:.2f}\033[0m")
                print(f"Saque realizado com sucesso! \033[34mSaldo atual: R$ {self.saldo:.2f}\033[0m")
            elif saque > self.limite:
                print(f"Limite de R${self.limite:.2f} por saque")
            elif self.numero_saques >= self.LIMITE_SAQUE:
                print("Limite de saques diários atingido.")
            elif saque < 0:
                print("O valor do saque deve ser maior que 0")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    def extrato_fun(self):
        print(f"\n============ EXTRATO ============\n")
        if self.extrato:
            for operacao in self.extrato:
                print(operacao)
        else:
            print("Não há movimentações.")
        print(f"\033[34mSaldo atual: R$ {self.saldo:.2f}\033[0m")

# Classe Cadastramento Bancario
class CadastramentoBancario:
    def __init__(self):
        self.dados_pessoas = []
        self.dados_contas = []
        self.contador_conta = 1

    def cadastro_user(self):
        cpf = input("Digite o CPF: ")
        for registro in self.dados_pessoas:
            if cpf == registro["cpf"]:
                print("CPF já cadastrado")
                return
        nome = input("Digite o nome: ")
        nascimento = input("Digite data de nascimento: ")
        endereco = input("Digite seu endereço: ")

        self.dados_pessoas.append({
            "cpf": cpf,
            "nome": nome,
            "nascimento": nascimento,
            "endereco": endereco
        })

        print("Cadastro concluído com sucesso!")

    def cadastrar_cont(self):
        cpf = input("Digite o CPF do titular da conta: ")

        usuario_encontrado = any(pessoa['cpf'] == cpf for pessoa in self.dados_pessoas)
        if not usuario_encontrado:
            print("Usuário não encontrado. Cadastre o usuário primeiro.")
            return

        nova_conta = {
            "agencia": "001",
            "numero_conta": self.contador_conta,
            "cpf": cpf,
            "conta_bancaria": ContaBancaria()
        }

        self.dados_contas.append(nova_conta)
        print(f"Conta {self.contador_conta} criada com sucesso para CPF {cpf}!")
        self.contador_conta += 1

    def ver_pessoas(self):
        if not self.dados_pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print("\nPessoas Cadastradas:")
        for pessoa in self.dados_pessoas:
            print(f"CPF: {pessoa['cpf']}, Nome: {pessoa['nome']}, Nascimento: {pessoa['nascimento']}, Endereço: {pessoa['endereco']}")

    def ver_contas(self):
        if not self.dados_contas:
            print("Nenhuma Conta cadastrada.")
            return

        print("\nContas Cadastradas:")
        for conta in self.dados_contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, CPF: {conta['cpf']}")


# Iniciando menu
conta = ContaBancaria()
cadastro = CadastramentoBancario()

while True:
    opcao = input(menu)

    if opcao == "1":
        cadastro.cadastro_user()
    elif opcao == "2":
        cadastro.cadastrar_cont()
    elif opcao == "3":
        cadastro.ver_pessoas()
    elif opcao == "4":
        cadastro.ver_contas()
    elif opcao == "5":
        cpf = input("Digite o CPF do titular: ")
        contas_do_cpf = [c for c in cadastro.dados_contas if c["cpf"] == cpf]

        if not contas_do_cpf:
            print("Nenhuma conta encontrada para este CPF.")
            continue

        print("\nContas disponíveis:")
        for conta in contas_do_cpf:
            print(f"Conta: {conta['numero_conta']} | Agência: {conta['agencia']}")

        numero = int(input("Digite o número da conta desejada: "))
        conta_selecionada = next((c for c in contas_do_cpf if c["numero_conta"] == numero), None)

        if conta_selecionada:
            conta_selecionada["conta_bancaria"].deposito_fun()
        else:
            print("Conta não encontrada.")

    elif opcao == "6":
        cpf = input("Digite o CPF do titular: ")
        contas_do_cpf = [c for c in cadastro.dados_contas if c["cpf"] == cpf]

        if not contas_do_cpf:
            print("Nenhuma conta encontrada para este CPF.")
            continue

        print("\nContas disponíveis:")
        for conta in contas_do_cpf:
            print(f"Conta: {conta['numero_conta']} | Agência: {conta['agencia']}")

        numero = int(input("Digite o número da conta desejada: "))
        conta_selecionada = next((c for c in contas_do_cpf if c["numero_conta"] == numero), None)

        if conta_selecionada:
            conta_selecionada["conta_bancaria"].saque_fun()
        else:
            print("Conta não encontrada.")

    elif opcao == "7":
        cpf = input("Digite o CPF do titular: ")
        contas_do_cpf = [c for c in cadastro.dados_contas if c["cpf"] == cpf]

        if not contas_do_cpf:
            print("Nenhuma conta encontrada para este CPF.")
            continue

        print("\nContas disponíveis:")
        for conta in contas_do_cpf:
            print(f"Conta: {conta['numero_conta']} | Agência: {conta['agencia']}")

        numero = int(input("Digite o número da conta desejada: "))
        conta_selecionada = next((c for c in contas_do_cpf if c["numero_conta"] == numero), None)

        if conta_selecionada:
            conta_selecionada["conta_bancaria"].extrato_fun()
        else:
            print("Conta não encontrada.")

    elif opcao == "8":
        print("Encerrando o sistema bancário...")
        break
    else:
        print("Opção inválida. Tente novamente.")
