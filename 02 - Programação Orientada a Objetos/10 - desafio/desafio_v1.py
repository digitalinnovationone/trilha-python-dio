import textwrap
from datetime import datetime
from abc import ABC, abstractmethod
class Cliente:
    def __init__(self, id, endereco):
        self._id = id     
        self._contas = []
        self._endereco = endereco

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def cadastrar_conta(self, conta):
        self._contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, id, endereco):
        super().__init__(id, endereco)

        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._agencia = "0001"
        
        self._saldo = 0
        self._cliente = cliente
        self._historico = Historico()

    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            
            print(f"Saldo atual é de R${self.saldo:.2f}.")
        else:
            print("Valor inválido para depósito.")
            return False
        return True
    
    def sacar(self, valor):
        saldo = self._saldo
        
        if valor > self._saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        
        elif valor > 0:
            self._saldo -= valor
           
            
            print(f"Saque realizado com sucesso! Saldo atual é de R${self.saldo:.2f}.")
            return True

        else:
            print("Operação falhou! O valor do saque deve ser positivo.")

        return False    

    
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
                   
    
class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite=500, numero_saques=0, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._numero_saques = numero_saques
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)    

    def sacar(self, valor): 
        if self._numero_saques >= self._limite_saques:
            print('Operação falhou! Número máximo de saques excedido.')
            return False
        elif valor > self._limite:
            print('Operação falhou! O valor do saque excede o limite.')
            return False

        elif valor > self._saldo and valor < self._limite:
            print('Operação falhou! Você não tem saldo suficiente.')
            return False

        elif valor > 0:
            self._saldo -= valor
            
            self._numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual é de R${self.saldo:.2f}.")
            return True
        else:
            print("Operação falhou! O valor do saque deve ser positivo.")
        return False
       
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self._cliente.nome}
        """
          

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
            )
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    

class Transacao(ABC): 
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        pass
    
    def registrar(self, conta):
        pass

    

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self._valor = valor

    @property
    def valor(self):
        return self._valor    

    def registrar(self, conta):
        sucesso_deposito = conta.depositar(self.valor)
        if sucesso_deposito:                   
            conta.historico.adicionar_transacao(self)
        

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_saque = conta.sacar(self.valor)

        if sucesso_saque:
            conta.historico.adicionar_transacao(self)

def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "")

def pegar_cliente(cpf, clientes):

    cliente = [cliente for cliente in clientes if cliente._cpf == limpar_cpf(cpf)]
    return cliente[0] if cliente else None

def pegar_conta(numero, contas):

    conta_cliente = [conta for conta in contas if conta._numero == numero]
    
    return conta_cliente[0] if conta_cliente else None

def gerat_id_cliente(clientes):
    if not clientes:
        return 1
    else:
        return max(cliente._id for cliente in clientes) + 1

def menu():
    
    
    menu = """\n
    ==========Banco do Daniel===========

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Cliente
    [cc] Cadastrar Conta Bancária
    [l] Listar Clientes
    [lc] Listar Contas Bancárias
    [q] Sair

    ====================================
    

    => """
    escolha =  input(textwrap.dedent(menu).strip())
    return escolha.lower()

def cadastrar_cliente(clientes: list):

    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do cliente (apenas números): ").replace(".", "").replace("-", "")
    
    if any(cliente._cpf == cpf for cliente in clientes):
        print("CPF já cadastrado. Tente novamente.")
        return
    
    endereco = input("Digite o endereço do cliente (Logradouro, número - Bairro - Cidade/UF): ")

    id_cliente = gerat_id_cliente(clientes)

    cliente = Pessoa_Fisica(id=id_cliente, nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)



    print(f"Cliente {nome} cadastrado com sucesso!")

def cadastrar_conta(clientes: list, contas: list):
    
    numero_conta = len(contas) + 1 
    cpf = input("Digite o CPF do cliente para vincular a conta: ").replace(".", "").replace("-", "")
    if not any(cliente._cpf == cpf for cliente in clientes):
        print("CPF não cadastrado. Por favor, cadastre o cliente primeiro.")
        return
    cliente = next(cliente for cliente in clientes if cliente._cpf == cpf)
    saldo = 0
    conta = Conta_Corrente.nova_conta(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    
    print(f"Conta cadastrada com sucesso!")

def listar_clientes(clientes: list):

    if not clientes:
        print("Erro: Nenhum cliente cadastrado.")
        return
    print("\nLista de Clientes:")
    for cliente in clientes:
        print(f"\nId: {cliente._id}, Nome: {cliente._nome}, Cpf: {cliente._cpf}.")

def listar_contas(contas: list):

    if not contas:
        print("Erro: Nenhuma conta bancária cadastrada.")
        return
    print("\nLista de Contas Bancárias:")
    for conta in contas:
        print(f"\nNúmero da Conta: {conta._numero}, Agência: {conta._agencia}, Titular: {conta.cliente._nome})")

def deposito(contas: list):
        

        numero = int(input("digite o número da conta que deseja fazer o depósito: "))
        conta_cliente = pegar_conta(numero, contas)
        if not conta_cliente:
            print("Conta não encontrada.")
            return False

        valor_a_depositar = float(input("Digite o valor que deseja depositar"))

        transacao = Deposito(valor_a_depositar)
        print(f"Depósito de R$ {transacao.valor:.2f} realizado com sucesso!")

        cliente = conta_cliente.cliente
        cliente.realizar_transacao(conta_cliente, transacao)
        
        return True

        
def saque(contas: list):
        conta_cliente = int(input("Digite o número da conta que deseja fazer o saque: "))
        conta = pegar_conta(conta_cliente, contas)
        if not conta:
            print("Conta não encontrada.")
            return False 
        valor_a_sacar = float(input("Digite o valor que deseja sacar."))

        transacao = Saque(valor_a_sacar)
        cliente = conta.cliente
        
        cliente.realizar_transacao(conta, transacao)
        print(f"Saque de R$ {transacao.valor:.2f} realizado com sucesso!")

def extrato(contas: list): 
    conta = int(input("Digite o número da conta que deseja ver o extrato: "))
    conta_cliente = pegar_conta(conta, contas)

    
    if not conta:
        print("Conta não encontrada.")
        return False
    
    
    print("\n================ EXTRATO ================")
    for transacao in conta_cliente.historico.transacoes:
        print(f"\n{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
    print("Não foram realizadas movimentações." if not transacao in conta_cliente.historico.transacoes else "")
    print(f"\nSaldo: R$ {conta_cliente._saldo:.2f}")
    print("==========================================")

def main():
    escolha = ""
    clientes = []
    contas = []
    
    while escolha != "q" and escolha != "Q":

        escolha = menu()
        
        if escolha == "s":
           saque(contas)    

        elif escolha == "d":
            deposito(contas)

        elif escolha == "c":    
            cadastrar_cliente(clientes)

        elif escolha == "cc":  
            cadastrar_conta(clientes, contas)

        elif escolha == "l":
            listar_clientes(clientes)

        elif escolha == "lc":
            listar_contas(contas)
              
        elif escolha == "e":
            extrato(contas)       

        elif escolha =="q": 
            print('Encerrando a operação')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
           
       
              
if __name__ == "__main__":
    main()
