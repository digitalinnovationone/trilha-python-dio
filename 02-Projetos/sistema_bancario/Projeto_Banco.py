# Projeto_Banco.py

class ContaBancaria:
    """
    Representa uma conta bancária com operações de depósito, levantamento,
    consulta de saldo e extrato.
    """

    def __init__(self, titular, saldo=0, limite=500, limite_saques=3):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): O nome do titular da conta.
            saldo (float): Saldo inicial da conta.
            limite (float): Limite de valor por saque.
            limite_saques (int): Número máximo de saques diários.
        """
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = limite_saques

    def depositar(self, valor):
        """Adiciona dinheiro à conta e atualiza o extrato."""
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        """Retira dinheiro da conta e atualiza o extrato, com validações."""
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self.limite:.2f}.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        """Mostra o histórico de movimentações e o saldo atual."""
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


# --- Programa Principal ---

def main():
    """
    Executa o programa principal com o menu interativo.
    """
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    conta_principal = ContaBancaria("Usuário Principal")

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta_principal.depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta_principal.sacar(valor)

        elif opcao == "e":
            conta_principal.exibir_extrato()

        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()