# Sistema Bancário em Python

## Descrição do Projeto

Este projeto implementa um sistema bancário simples em Python, com três operações básicas: depósito, saque e visualização de extrato. O sistema é projetado para um único usuário e oferece funcionalidades essenciais para a gestão de uma conta bancária.

## Funcionalidades

### 1. Depósito

- O usuário pode depositar valores positivos na conta bancária.
- Todos os depósitos são armazenados em uma lista e exibidos na operação de extrato.
- O saldo da conta é atualizado com cada depósito realizado.

### 2. Saque

- O usuário pode realizar até 3 saques diários, com um limite máximo de R$ 500,00 por saque.
- O sistema verifica se o usuário tem saldo suficiente antes de permitir o saque.
- Todos os saques são armazenados em uma lista e exibidos na operação de extrato.
- O saldo da conta é atualizado com cada saque realizado.

### 3. Extrato

- O extrato lista todos os depósitos e saques realizados na conta.
- Exibe o saldo atual da conta no final da listagem.
- Se não houver movimentações, exibe a mensagem: "Não foram realizadas movimentações".
- Os valores são exibidos no formato R$ xxx.xx.

## Estrutura do Código

### Variáveis Globais

- `saldo`: Armazena o saldo atual da conta.
- `depositos`: Lista que armazena todos os depósitos realizados.
- `saques`: Lista que armazena todos os saques realizados.
- `saques_diarios`: Dicionário que armazena o número de saques realizados por dia.

### Funções

- `depositar(valor)`: Realiza um depósito na conta se o valor for positivo.
- `sacar(valor)`: Realiza um saque da conta, respeitando os limites diários e o saldo disponível.
- `extrato()`: Exibe o extrato com todos os depósitos, saques e o saldo atual.
- `menu()`: Exibe o menu de opções e chama as funções apropriadas com base na escolha do usuário.

### Execução

Para iniciar o sistema bancário, execute a função `menu()`, que exibirá o menu de opções e permitirá ao usuário interagir com o sistema.

## Como Executar

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Salve o código em um arquivo com a extensão `.py`, por exemplo, `sistema_bancario.py`.
3. Execute o arquivo pelo terminal ou prompt de comando com o seguinte comando: `python sistema_bancario.py`
4. Siga as instruções exibidas no menu para realizar depósitos, saques e visualizar o extrato.

## Exemplo de Uso

--- Sistema Bancário ---

    Depositar
    Sacar
    Extrato
    Sair
    Escolha uma opção: 1
    Informe o valor para depósito: R$ 1000.00
    Depósito de R$ 1000.00 realizado com sucesso!

Escolha uma opção: 2
Informe o valor para saque: R$ 500.00
Saque de R$ 500.00 realizado com sucesso!

Escolha uma opção: 3
Extrato bancário:
Depósitos:
R$ 1000.00
Saques:
R$ 500.00
Saldo atual: R$ 500.00

## Conclusão

Este projeto fornece uma base para um sistema bancário simples, demonstrando conceitos fundamentais de programação em Python, como manipulação de variáveis, listas, dicionários e controle de fluxo. Pode ser expandido para incluir funcionalidades mais avançadas, como suporte a múltiplos usuários e persistência de dados em um banco de dados.
