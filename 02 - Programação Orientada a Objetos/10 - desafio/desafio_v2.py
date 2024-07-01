from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adc_conta(self, conta):
        self.contas.append(conta)
    

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.saldo = 0
        self.agencia = "1010"
        self.cliente = cliente
        self.historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('Operação falhou! O seu saldo é insuficiente.')
        
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso!')
            return True
        
        else:
            print('Operação falhou. O valor informado é inválido.')
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso!')
        else:
            print('Operação falhou. O valor informado é inválido.')
            return False
        return True
    
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, qtd_saques=3):
        super().__init__(numero, cliente)
        self.limite_saques = qtd_saques
        self.limite = limite
        
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.
                             transacao if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.qtd_saques
        
        if excedeu_limite:
            print('Operação falhou! O valor do saque excede seu limite.')
            
        elif excedeu_saques:
            print('Operação falhou! Você excedeu o limite de saques.')
        
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.titular.nome}'''


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, limite=800, qtd_saques=5):
        super().__init__(numero, cliente, limite, qtd_saques)
        self.limite_saques = qtd_saques
        self.limite = limite
        
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.
                             transacao if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.qtd_saques
        
        if excedeu_limite:
            print('Operação falhou! O valor do saque excede seu limite.')
            
        elif excedeu_saques:
            print('Operação falhou! Você excedeu o limite de saques.')
        
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/P:\t\t{self.numero}
            Titular:\t{self.titular.nome}'''

class Historico:
    def __init__(self):
        self.transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adc_transacao(self, transacao):
        
        #dicionário
        self._transacoes.append({
                                 "tipo": transacao.__class__.__name__,
                                 "valor": transacao.valor,
                                 "data": datetime.now().strftime
                                 ("%d-%m-%Y %H:%M:%s"),})


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(cls, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adc_transacao(self)
            

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adc_transacao(self)


def menu():
    menu_texto = '''
    \t\t MENU INICIAL \t\t

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar uma nova conta
    [6] Listar o Usuário
    [0] Sair

    Digite a operação desejada: '''
    return input(menu_texto)

# depósito
def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtro_usuarios(cpf, clientes)
    
    if not cliente:
        print('\tUsuário não encontrado!')
        return 
    
    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)
    
    conta = recuperar_usuarios(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

# saque
def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtro_usuarios(cpf, clientes)
    
    if not cliente:
        print('\tUsuário não encontrado!')
        return
    
    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)
    
    conta = recuperar_usuarios(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(transacao, conta)

def mostrar_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtro_usuarios(cpf, clientes)
    
    if not cliente:
        print('\tUsuário não encontrado!')
        return
    
    conta = recuperar_usuarios(cliente)
    if not conta:
        return
    
    print('\n\t\t\tEXTRATO\t\t\t')
    transacoes = conta.historico.transacoes
    
    extrato = ''
    if not transacoes:
        extrato = 'Nâo foram realizadas movimentações.'
    else: 
        for transacao in transacoes:
            extrato += f'\n{transacao["tipo"]} - R$ {transacao["valor"]:.2f} - {transacao["data"]}'
    
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')


def filtro_usuarios(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
    

def recuperar_usuarios(cliente):
    if not cliente.contas:
        print('Cliente não possui conta!')
        return
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def criando_usuario(usuarios):
    cpf = input('\nInforme o CPF do usuário: ')
    usuario = filtro_usuarios(cpf, usuarios)
    
    if usuario:
        print('\tUsuário já existe!')
        return
    
    nome = input('Informe o seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o seu endereço (Rua, número, bairro - Cidade / Estado em sigla): ')

    cliente = PessoaFisica(nome=nome, data_nasc=data_nascimento, cpf=cpf, endereco=endereco)

    usuarios.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtro_usuarios(cpf, usuarios)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listagem(contas):
    for conta in contas:
        lista_texto = f'''
        Agência: {conta['agencia']}
        Conta(C/C): {conta['numeroConta']}
        Titular da Conta: {conta['usuario']['nome']}
        '''
        print(lista_texto)
        

def main():
    clientes =[]
    contas = []
    
    while True:
        opcao = menu()
        if opcao == '0':
            print("Saindo...")
            break

        elif opcao == '1':
            depositar(clientes)
        elif opcao == '2':
            sacar(clientes)
        elif opcao == '3':
            mostrar_extrato(clientes)
        elif opcao == '4':
            criando_usuario(clientes)
        elif opcao == '5':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)    
        elif opcao == '6':
            listagem(contas)
        elif opcao == '0':
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
        
main()
