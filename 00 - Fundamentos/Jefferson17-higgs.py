# sistema bancario

conta_bancaria= 3000.00
limite_diario_saques= 0
lista_deposistos= []
lista_saques= []

MENU= 'Menu'
EXTRATO= 'Extrato'
extrato= ''
while True:
    
    print('')
    print(MENU.center(24, '-'))
    menu= '''\n
          
    1. Deposito
    2. Saque
    3. Extrato
    4. Sair
          
    Opção =>  '''
    escolha_usuario= int(input(menu))
    print('-'*24,'\n')

    if escolha_usuario == 1:
        
        print(f'\nSaldo em conta: {conta_bancaria:.2f}')
        deposito_usuario= int(input('Digite o valor de deposito: '))
        
        permitir_deposito= conta_bancaria+deposito_usuario  if deposito_usuario > 0 else 'Valor invalido, selecione outro valor.'
        conta_bancaria= permitir_deposito
        extrato+= f'Deposito: R$ {deposito_usuario:.2f}\n' 
        print(f'Saldo atual: {conta_bancaria:.2f}' if type(permitir_deposito) != str else permitir_deposito)
      
    elif escolha_usuario == 2:
        
            saque_usuario= int(input('\nDigite o valor de saque: '))
            
            if saque_usuario <= 500:
                
                limite_diario_saques+= 1
                
                if limite_diario_saques <= 3:
                
                    permitir_saque= conta_bancaria-saque_usuario if conta_bancaria > 0 else 'Não a saudo suficiente'
                    conta_bancaria= permitir_saque
                    extrato+= f'Saque: {saque_usuario:.2f}\n'
                    print(f'Saldo atual: {conta_bancaria:.2f}' if type(permitir_saque) != str else permitir_saque)
                
                else:
                    
                    print('Limite diario de saques excedido.')
                                
            else:
                
                print('Limite de R$ 500.00 excedido.')
                
    elif escolha_usuario == 3:
                   
        print('')
        print(EXTRATO.center(27, '-'),'\n')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {conta_bancaria:.2f}")
        print('-'*24,'\n')
       
    elif escolha_usuario == 4:
        
        print('\nOperação encerrada, obrigado.')
        break
    
    else:
        
        print('\nValor invalido, digite um valor valido.')
        