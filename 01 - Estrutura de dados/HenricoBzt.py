# Uma nova versão do projeto de banco com a implementaçção de funções.

menu = """" 

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[n] Nova conta
[q] Sair 

=> """
contas = []
usuarios = []
saldoa = 0
limite = 500
extratob = " "
numero_de_saques = 0
nmrconta = 1
LIMITE_SAQUES = 3
AGENCIA = '0001'
def deposito(saldo, valor, extrato,/):
            print('Depósito')
            if valor > 0:
                saldo += valor   #adiciona o deposito ao saldo
                extrato += f'Déposito: R$ {valor:.2f}\n'
            else:
                print('Operação invalida, digite um valor válido.')
            return saldo, extrato

def fazer_saque(*,saldo, valor_saque, extrato, numero_saque, limite_diario,limite):
     execedeu_saldo = valor_saque > saldo
     exedeu_limite_valor = valor_saque > limite
     execedeu_limite_saque = numero_saque >= limite_diario
    
     if execedeu_saldo:
           print('Operacão inválida!, saldo insuficiente.')
     elif exedeu_limite_valor:
           print('Operação inválida!, saque execedeu limite de R$ 500')
     elif execedeu_limite_saque:
           print('Operação falhou!, você execedeu limite de saque diário.')
     elif saldo > valor_saque:
           saldo -= valor_saque
           extrato +=  f'Saque: R${valor_saque:.2f}\n'
           numero_saque += 1
     else:
           print('Operação falhou, digite um valor válido.')
     return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
        print('\n===================Extrato======================')
        print('Não foram feitas movimentações.') if not extratob else extratob
        print(f'{extrato}' )
        print(f' Saldo atual: R$ {saldo:.2f}')
        
def criar_usuario(usuario):
    cpf = input('Digite seu cpf(somente numeros): ')
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
         print('-----Já existe um usuário com este cpf.-----')
         return
    nome = input('Digite o seu nome: ')
    data_nascimento = input('Informe sua data de nascimento(dd/mm/ano): ')
    endereco = input('Informe o seu endereço ( logradouro, numero - bairro - cidade/sigla estado.): ')
    usuarios.append({'nome': nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    print('Criando usuário...')
    return(usuario)

def filtrar_usuario(cpf,usuarios):
     usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
     return usuario_filtrado[0] if usuario_filtrado else None

def nova_conta(agencia,numero_conta,usuarios):
    cpf = input('Digite seu cpf(Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
         print('=======Conta criada com Sucesso!======')
         return {'agencia': agencia, 'numero_conta': numero_conta, 'usuarios': usuarios}
    print('Usuário não encontrado!')
while True:
    opcao = input(menu)
    if opcao == 'd':
       valor = float(input('Digite um valor: ')) 
       saldoa, extratob = deposito(saldoa,valor, extratob)
    elif opcao == 's':
        valor= float(input('Insira o valor do saque: '))
        saldoa,extratob, = fazer_saque(
                            saldo=saldoa,
                            valor_saque=valor,
                            limite=limite,
                            extrato=extratob,
                            numero_saque=numero_de_saques,
                            limite_diario=LIMITE_SAQUES)
    elif opcao == 'c':
         criar_usuario(usuario= usuarios)
    elif opcao == 'e':
         exibir_extrato(saldoa,extrato=extratob)
    elif opcao == 'n':
         conta = nova_conta(AGENCIA, nmrconta, usuarios)
         if conta:
            contas.append(conta)
            nmrconta += 1
    elif opcao == 'q':
        break
    else:
        print('Operação invalida.')


        

# usuario = { 
#         'usuario_1': { 'nome': 'Henrico Pereira Bazante', 'data_nascimento' : '06/11/2006', 'cpf': '15729185430', 'endereço': 'araripina'}
#        }
