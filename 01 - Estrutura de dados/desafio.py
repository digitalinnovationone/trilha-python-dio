"""
Sistema Bancário - Gestão de Usuários e Contas

FUNCIONALIDADES E IMPLEMENTAÇÕES:

- Novo Usuário: Cadastro de uma pessoa física no sistema, informando nome, CPF, data de nascimento e endereço.
  Cada usuário pode ter uma ou mais contas bancárias associadas ao seu CPF.

- Nova Conta: Abertura de uma conta bancária para um usuário já cadastrado. Cada conta tem número único sequencial,
  senha de 4 dígitos aleatórios, saldo inicial de R$ 500,00, extrato e contador de saques, e está vinculada a um usuário existente.

- Login: O usuário acessa o sistema informando número da conta e senha. Apenas a conta autenticada pode realizar operações.

- Depósito: Permite depósitos apenas de valores positivos, atualizando saldo e extrato da conta autenticada.

- Saque: Permite até 3 saques diários de até R$ 500,00 cada, respeitando o saldo disponível e atualizando extrato e contador.

- Extrato: Exibe todas as movimentações da conta autenticada e o saldo, com formatação brasileira (ex: R$ 1.000,00).

- Redefinir Senha: Permite ao usuário redefinir a senha da conta autenticada, exigindo 4 dígitos numéricos.

- Listar Contas: Exibe todas as contas cadastradas, mostrando agência, número, titular e saldo de cada uma, com valores formatados.

- Persistência: Todos os dados de usuários e contas são salvos e carregados automaticamente em arquivo JSON.

- Formatação Brasileira: Todos os valores monetários são exibidos no padrão brasileiro, com separador de milhar e duas casas decimais (ex: R$ 1.000,00, R$ 100,45, R$ 1.000.200,01).

Fluxo recomendado:
1. Criar novo usuário (caso ainda não exista).
2. Criar nova conta para o usuário já cadastrado.
3. Realizar login com número da conta e senha para acessar operações bancárias.
4. Realizar depósitos, saques, consultar extrato, redefinir senha ou sair.

"""

import json
import os

def carregar_dados():
    caminho = "01 - Estrutura de dados/banco_dados.json"
    if not os.path.exists(caminho):
        return [], []
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados.get("usuarios", []), dados.get("contas", [])

def salvar_dados(usuarios, contas):
    caminho = "01 - Estrutura de dados/banco_dados.json"
    diretorio = os.path.dirname(caminho)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump({"usuarios": usuarios, "contas": contas}, f, ensure_ascii=False, indent=2)
import textwrap


def menu(autenticado=False, conta_logada=None):
    if autenticado and conta_logada:
        menu = f"""\n
        ================ MENU ================
        Conta: {conta_logada['numero_conta']}
        1. Depositar
        2. Sacar
        3. Extrato
        4. Redefinir senha
        5. Logout
        0. Sair
        => """
    else:
        menu = """\n
        ================ MENU ================
        1. Criar novo usuário
        2. Criar nova conta
        3. Login
        4. Listar contas
        0. Sair
        => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    """
    Realiza um depósito na conta, aceitando apenas valores positivos.

    Exemplos:
    - Depósito de R$ 100,00: saldo passa de R$ 0,00 para R$ 100,00 e extrato registra "Depósito: R$ 100.00".
    - Depósito de R$ -50,00: operação rejeitada, saldo e extrato permanecem inalterados.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t{formatar_real(valor)}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque na conta, respeitando limites diários e por valor.

    Regras:
    - Até 3 saques por dia.
    - Limite de R$500,00 por saque.
    - Não permite saque maior que o saldo.
    - Apenas valores positivos.

    Exemplos:
    - Saque de R$ 200,00 com saldo suficiente: saldo reduzido, extrato atualizado, contador incrementado.
    - Saque de R$ 600,00: operação rejeitada por exceder o limite.
    - Quarto saque no mesmo dia: operação rejeitada por exceder o número de saques.
    - Saque de valor negativo: operação rejeitada.

    """
    excedeu_saldo = valor > saldo or valor <= 0
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    elif excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor <= saldo:
        saldo -= valor
        extrato += f"Saque:\t\t{formatar_real(valor)}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t{formatar_real(saldo)}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ").strip()
    if not cpf:
        print("\n@@@ CPF não pode ser vazio! @@@")
        return
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ").strip()
    if not nome:
        print("\n@@@ Nome não pode ser vazio! @@@")
        return
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    if not data_nascimento:
        print("\n@@@ Data de nascimento não pode ser vazia! @@@")
        return
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    if not endereco:
        print("\n@@@ Endereço não pode ser vazio! @@@")
        return

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


import random

def gerar_senha():
    return f"{random.randint(0, 9999):04d}"

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        senha = gerar_senha()
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 500,
            "extrato": "",
            "numero_saques": 0,
            "senha": senha
        }
        print(f"\n=== Conta criada com sucesso! ===")
        print(f"Titular: {usuario['nome']}")
        print(f"Número da conta: {numero_conta}")
        print(f"Senha inicial: {senha}")
        return conta

def autenticar_conta(contas):
    numero = input("Informe o número da conta: ").strip()
    senha = input("Informe a senha de 4 dígitos: ").strip()
    for conta in contas:
        if str(conta["numero_conta"]) == numero and conta["senha"] == senha:
            print("\nLogin realizado com sucesso!")
            return conta
    print("\n@@@ Número de conta ou senha inválidos! @@@")
    return None
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def redefinir_senha(conta):
    nova_senha = input("Digite a nova senha de 4 dígitos: ").strip()
    if not (nova_senha.isdigit() and len(nova_senha) == 4):
        print("\n@@@ Senha inválida! Deve conter exatamente 4 dígitos numéricos. @@@")
        return
    conta["senha"] = nova_senha
    print("\nSenha redefinida com sucesso!")


def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def listar_contas(contas):
    for conta in contas:
        saldo_formatado = formatar_real(conta.get('saldo', 0))
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\t{saldo_formatado}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    limite = 500

    usuarios, contas = carregar_dados()
    conta_logada = None

    while True:
        opcao = menu(autenticado=conta_logada is not None, conta_logada=conta_logada)

        if conta_logada:
            if opcao == "1":
                valor = float(input("Informe o valor do depósito: "))
                conta_logada["saldo"], conta_logada["extrato"] = depositar(
                    conta_logada["saldo"], valor, conta_logada["extrato"]
                )

            elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))
                conta_logada["saldo"], conta_logada["extrato"], conta_logada["numero_saques"] = sacar(
                    saldo=conta_logada["saldo"],
                    valor=valor,
                    extrato=conta_logada["extrato"],
                    limite=limite,
                    numero_saques=conta_logada["numero_saques"],
                    limite_saques=LIMITE_SAQUES,
                )

            elif opcao == "3":
                exibir_extrato(conta_logada["saldo"], extrato=conta_logada["extrato"])

            elif opcao == "4":
                redefinir_senha(conta_logada)

            elif opcao == "5":
                conta_logada = None
                print("\nLogout realizado com sucesso!")

            elif opcao == "0":
                salvar_dados(usuarios, contas)
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

        else:
            if opcao == "1":
                criar_usuario(usuarios)

            elif opcao == "2":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            elif opcao == "3":
                conta_logada = autenticar_conta(contas)

            elif opcao == "4":
                listar_contas(contas)

            elif opcao == "0":
                salvar_dados(usuarios, contas)
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
