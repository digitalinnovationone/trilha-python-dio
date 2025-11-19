#!/usr/bin/env python3
import re
from typing import Dict, List, Tuple, Optional

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=> """

# Estruturas de dados
usuarios: List[Dict] = []   # cada usuário: {"nome","data_nascimento","cpf","endereco"}
contas: List[Dict] = []    # cada conta: {"agencia","numero","usuario","saldo","limite","extrato","numero_saques"}
PROXIMO_NUMERO_CONTA = 1
AGENCIA_PADRAO = "0001"
LIMITE_PADRAO = 500.0
LIMITE_SAQUES_PADRAO = 3

# -------------------------
# Funções pedidas pelo enunciado
# -------------------------

# Saque -> apenas keyword-only
def sacar(*, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, limite_saques: int) -> Tuple[float, str, int, str]:
    """
    Recebe somente por nome (keyword-only).
    Retorna (novo_saldo, novo_extrato, novo_numero_saques, mensagem).
    """
    mensagem = ""
    if valor <= 0:
        mensagem = "Operação falhou! O valor informado é inválido."
        return saldo, extrato, numero_saques, mensagem

    if valor > saldo:
        mensagem = "Operação falhou! Você não tem saldo suficiente."
        return saldo, extrato, numero_saques, mensagem

    if valor > limite:
        mensagem = "Operação falhou! O valor do saque excede o limite."
        return saldo, extrato, numero_saques, mensagem

    if numero_saques >= limite_saques:
        mensagem = "Operação falhou! Número máximo de saques excedido."
        return saldo, extrato, numero_saques, mensagem

    # se passou por todas as checagens:
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    mensagem = f"Saque de R$ {valor:.2f} realizado com sucesso."
    return saldo, extrato, numero_saques, mensagem


# Depósito -> positional-only
def depositar(saldo: float, valor: float, extrato: str, /) -> Tuple[float, str, str]:
    """
    Recebe apenas por posição (positional-only).
    Retorna (novo_saldo, novo_extrato, mensagem).
    """
    mensagem = ""
    if valor <= 0:
        mensagem = "Operação falhou! O valor informado é inválido."
        return saldo, extrato, mensagem

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    mensagem = f"Depósito de R$ {valor:.2f} realizado com sucesso."
    return saldo, extrato, mensagem


# Extrato -> positional only + keyword only
def mostrar_extrato(saldo: float, /, *, extrato: str) -> None:
    """
    Recebe saldo como positional-only e extrato como keyword-only.
    Apenas imprime o extrato.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato, end="")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================\n")


# -------------------------
# Novas funções: criar usuário e criar conta
# -------------------------

def limpar_cpf(cpf_raw: str) -> str:
    """Remove tudo que não for dígito do CPF e retorna só dígitos."""
    return re.sub(r"\D", "", cpf_raw)


def existe_usuario_por_cpf(cpf: str) -> bool:
    cpf = limpar_cpf(cpf)
    for u in usuarios:
        if u["cpf"] == cpf:
            return True
    return False


def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str) -> Tuple[bool, str]:
    """
    Cria um usuário e o adiciona à lista 'usuarios'.
    Retorna (sucesso, mensagem).
    """
    cpf_clean = limpar_cpf(cpf)
    if len(cpf_clean) != 11:
        return False, "CPF inválido: deve conter 11 dígitos."

    if existe_usuario_por_cpf(cpf_clean):
        return False, "Já existe usuário com esse CPF."

    usuario = {
        "nome": nome.strip(),
        "data_nascimento": data_nascimento.strip(),
        "cpf": cpf_clean,
        "endereco": endereco.strip(),
    }
    usuarios.append(usuario)
    return True, "Usuário cadastrado com sucesso."


def buscar_usuario_por_cpf(cpf: str) -> Optional[Dict]:
    cpf_clean = limpar_cpf(cpf)
    for u in usuarios:
        if u["cpf"] == cpf_clean:
            return u
    return None


def criar_conta(usuario_cpf: str) -> Tuple[bool, str]:
    """
    Cria uma conta vinculada ao usuário cujo CPF for informado.
    Retorna (sucesso, mensagem).
    """
    global PROXIMO_NUMERO_CONTA
    usuario = buscar_usuario_por_cpf(usuario_cpf)
    if not usuario:
        return False, "Usuário não encontrado para o CPF informado."

    conta = {
        "agencia": AGENCIA_PADRAO,
        "numero": PROXIMO_NUMERO_CONTA,
        "usuario": usuario,
        "saldo": 0.0,
        "limite": LIMITE_PADRAO,
        "extrato": "",
        "numero_saques": 0,
        "limite_saques": LIMITE_SAQUES_PADRAO,
    }
    contas.append(conta)
    PROXIMO_NUMERO_CONTA += 1
    return True, f"Conta criada com sucesso. Agência: {conta['agencia']}  Número: {conta['numero']}"


def listar_contas() -> None:
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=== Contas cadastradas ===")
    for c in contas:
        usuario = c["usuario"]
        print(f"Agência: {c['agencia']} | Conta: {c['numero']} | Titular: {usuario['nome']} | CPF: {usuario['cpf']}")
    print("=========================\n")


# -------------------------
# Funções de seleção / interação
# -------------------------

def selecionar_conta() -> Optional[Dict]:
    """Pede agência e número e retorna a conta correspondente (ou None)."""
    if not contas:
        print("Não há contas cadastradas.")
        return None

    agencia = input("Informe a agência (ex: 0001): ").strip()
    try:
        numero = int(input("Informe o número da conta: "))
    except ValueError:
        print("Número de conta inválido.")
        return None

    for c in contas:
        if c["agencia"] == agencia and c["numero"] == numero:
            return c

    print("Conta não encontrada.")
    return None


# -------------------------
# Loop principal interativo
# -------------------------

def main_loop():
    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            conta = selecionar_conta()
            if not conta:
                continue

            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("Valor inválido.")
                continue

            novo_saldo, novo_extrato, mensagem = depositar(conta["saldo"], valor, conta["extrato"])
            conta["saldo"] = novo_saldo
            conta["extrato"] = novo_extrato
            print(mensagem)

        elif opcao == "s":
            conta = selecionar_conta()
            if not conta:
                continue

            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("Valor inválido.")
                continue

            saldo, extrato, numero_saques, mensagem = sacar(
                saldo=conta["saldo"],
                valor=valor,
                extrato=conta["extrato"],
                limite=conta["limite"],
                numero_saques=conta["numero_saques"],
                limite_saques=conta["limite_saques"]
            )
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            conta["numero_saques"] = numero_saques
            print(mensagem)

        elif opcao == "e":
            conta = selecionar_conta()
            if not conta:
                continue

            mostrar_extrato(conta["saldo"], extrato=conta["extrato"])

        elif opcao == "nu":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            cpf = input("CPF (somente números ou com pontuação): ")
            logradouro = input("Logradouro (ex: Rua ABC, 10): ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("UF (sigla): ")
            endereco = f"{logradouro} - {bairro} - {cidade}/{estado}"

            ok, msg = criar_usuario(nome, data_nascimento, cpf, endereco)
            print(msg)

        elif opcao == "nc":
            cpf_para_vinculo = input("Informe o CPF do usuário para vincular a conta: ")
            ok, msg = criar_conta(cpf_para_vinculo)
            print(msg)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            print("Encerrando. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main_loop()

