class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
                self.exibir_saldo()  # Exibe o saldo após o saque
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Função para menu de opções
def menu():
    print("\n--- Sistema Bancário ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Saldo")
    print("4. Sair")

# Função principal para interação com o usuário
def sistema_bancario():
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$"))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$"))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_saldo()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama o sistema bancário
sistema_bancario()

