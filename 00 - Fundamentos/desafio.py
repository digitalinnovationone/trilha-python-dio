
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Novo usuário
[l] Listar usuário
[n] Nova conta
[u] Listar contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios =[{}]
usuarios.clear()
contas =[{}]
contas.clear()

def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")


    return saldo,extrato

def func_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def deposito(saldo,valor,extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato

def novo_usuario(nome,data,cpf,endereco,/):
    jaCadastrado = False
    for usuario in usuarios:
        if(str(usuario.get("cpf")) == str(cpf)):
           print("usuário não cadastrado, pois cpf já foi cadastrado")
           jaCadastrado = True
           break
    
    if(jaCadastrado == False):
        usuario = {"nome": f"{nome}", "cpf": f"{cpf}", "data": f"{data}","endereco": f"{endereco}"}
        usuarios.append(usuario)
        print("usuário cadastrado com sucesso")

def listar_usuarios():
    print(f"Usuários: \n")
    if(len(usuarios) == 0):
        print("nenhum usuário cadastrado")
        return
    
    for usuario in usuarios:
        print("nome: "+str(usuario.get("nome"))+
              f"\nCpf: "+str (usuario.get("cpf"))+
              f"\nData Nascimento :"+
              str(usuario.get("data"))+
              f"\nEndereco: "+
              str(usuario.get("endereco")))

def listar_contas():
    print(f"Contas: \n")
    if(len(contas) == 0):
        print("nenhuma conta cadastrada")
        return
    
    for conta in contas:
        print("Agência: "+str(conta.get("agencia"))+
              f"\nNúmero: "+str (conta.get("numero"))+
              f"\nCpf :"+
              f"\nUsuário :"+
              dict(conta.get("usuario")).get("nome"))

def nova_conta():
  cpf = input("informe cpf do usuário para cadastrar conta:")
  usuarioCadastrado = False
  usuarioVincular = {}
  for usuario in usuarios:
      if(str(usuario.get("cpf")) == cpf):
          usuarioCadastrado = True
          usuarioVincular = usuario
          break
  if(usuarioCadastrado == False):
      print("Conta não cadastrada pois não tem usuário com o cpf informado")
      return
  
          
  agencia = "0001"
  numeroUltimo =0 
  if(len(contas)>0):
   numeroUltimo = int(contas[len(contas)-1].get("numero"))
  numero = numeroUltimo+1
  novaConta = {"agencia":f"{agencia}","numero":f"{numero}","usuario":usuarioVincular}
  contas.append(novaConta)
  print("Conta cadastrada com sucesso")
  return

while True:

    opcao = input(menu)
   
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        resposta = deposito(saldo,valor,extrato)
       
        saldo = resposta[0]
        extrato = resposta[1]
       
    elif opcao == "s":
        
         valor = float(input("Informe o valor do saque: "))
         resposta = saque(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques =LIMITE_SAQUES)
         saldo = resposta[0]
         extrato = resposta[1]
         

    elif opcao == "e":
       func_extrato(saldo,extrato=extrato)

    elif opcao == "q":
        break
    elif opcao == "c":
        nome = str(input("informe nome do usuário:"))
        data = str(input("informe data de nascimento (ex: 20/04/1987):"))
        cpfInformado = str(input("informe cpf(apenas número):"))
        logradouro = str(input("informe logradouro:"))
        numero = str(input("informe número:"))
        bairro = str(input("informe bairro:"))
        cidade = str(input("informe cidade:"))
        estado = str(input("informe estado(ex: PE):"))

        validado = False
        cpf = ""
        for letra in cpfInformado:
            if(letra.isdigit()):
                cpf += letra
        
        while(validado == False):
            
            if(nome is not "" and
               data is not "" and
               cpf is not "" and 
               logradouro is not "" and
               bairro is not "" and
               cidade is not "" and
               estado is not ""):
                validado = True
            
            if(validado == False):
                print("faltou informa dados paracadastrar usuario, informe novamente")
                nome = str(input("informe nome do usuário:"))
                data = str(input("informe data de nascimento (ex: 20/04/1987):"))
                cpf = str(input("informe cpf(apenas número):"))
                logradouro = str(input("informe logradouro:"))
                numero = str(input("informe número:"))
                bairro = str(input("informe bairro:"))
                cidade = str(input("informe cidade:"))
                estado = str(input("informe estado(ex: PE):"))

        endereco = f"{logradouro}, {numero} - {bairro} {cidade}/{estado}"
        novo_usuario(nome,data,cpf,endereco)
    elif opcao == "l":
        listar_usuarios()
    elif opcao == "u":
        listar_contas()
    elif opcao == "n":
        nova_conta()
         
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
