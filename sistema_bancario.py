# Texto com as opções do menu, que será mostrado a cada repetição
menu = """

[d] Depositar
[s] Sacar
[r] Reiniciar conta
[e] Extrato
[q] Sair

=> """

# Variável que armazena o saldo da conta
saldo = 0

# Valor máximo permitido por saque
limite = 500

# Histórico de movimentações (depósitos e saques)
extrato = ""

# Contador de saques realizados no dia
numero_saques = 0

# Limite de saques que o usuário pode fazer por dia
LIMITE_SAQUES = 3

# Loop principal do sistema: continua até o usuário escolher sair
while True:

    # Exibe o menu e recebe a escolha do usuário
    opcao = input(menu)

    # Se o usuário escolher "d", será realizado um depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Só permite depositar valores positivos
        if valor > 0:
            saldo += valor                     # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Se o usuário escolher "s", será realizado um saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o usuário tem saldo suficiente
        excedeu_saldo = valor > saldo

        # Verifica se o valor do saque ultrapassa o limite permitido
        excedeu_limite = valor > limite

        # Verifica se o número máximo de saques foi atingido
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Exibe mensagens de erro apropriadas, se necessário
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        # Se o valor for válido e nenhuma das restrições for violada
        elif valor > 0:
            saldo -= valor                              # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"        # Registra no extrato
            numero_saques += 1                           # Incrementa o contador de saques

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Se o usuário escolher "e", o extrato será exibido
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        # Verifica se houve movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Se o usuário escolher "r", a conta reinicia
    elif opcao == "r":
        saldo = 0
        extrato = ""
        numero_saques = 0
        print("\nConta reiniciada com sucesso!\n")


    # Se o usuário escolher "q", o sistema será encerrado
    elif opcao == "q":
        break

    # Se o usuário digitar uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


