import textwrap


def menu():
    return input(textwrap.dedent("""
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """))


def ler_valor(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        print("\n@@@ Entrada inválida. @@@")
        return None


def normalizar_cpf(cpf):
    return "".join(filter(str.isdigit, cpf))


def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("\n@@@ Valor inválido. @@@")
        return saldo, extrato

    saldo += valor
    extrato.append(f"Depósito:\tR$ {valor:.2f}")
    print("\n=== Depósito realizado! ===")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n@@@ Valor inválido. @@@")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("\n@@@ Saldo insuficiente. @@@")
        return saldo, extrato, numero_saques

    if valor > limite:
        print("\n@@@ Excede o limite. @@@")
        return saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("\n@@@ Limite de saques atingido. @@@")
        return saldo, extrato, numero_saques

    saldo -= valor
    extrato.append(f"Saque:\t\tR$ {valor:.2f}")
    numero_saques += 1

    print("\n=== Saque realizado! ===")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")

    if not extrato:
        print("Não houve movimentações.")
    else:
        for item in extrato:
            print(item)

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")


def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)


def criar_usuario(usuarios):
    cpf = normalizar_cpf(input("CPF: "))

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Usuário já existe! @@@")
        return

    usuarios.append({
        "nome": input("Nome: "),
        "data_nascimento": input("Nascimento: "),
        "cpf": cpf,
        "endereco": input("Endereço: ")
    })

    print("=== Usuário criado! ===")


def criar_conta(agencia, numero, usuarios):
    cpf = normalizar_cpf(input("CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado. @@@")
        return None

    print("\n=== Conta criada! ===")
    return {
        "agencia": agencia,
        "numero": numero,
        "usuario": usuario.copy()
    }


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    for c in contas:
        print("=" * 40)
        print(f"Agência:\t{c['agencia']}")
        print(f"Conta:\t\t{c['numero']}")
        print(f"Titular:\t{c['usuario']['nome']}")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = ler_valor("Valor: ")
            if valor is None:
                continue
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = ler_valor("Valor: ")
            if valor is None:
                continue
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, limite,
                numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
