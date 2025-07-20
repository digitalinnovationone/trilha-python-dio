
# 💰 Sistema Bancário em Python — V3.0

Este projeto foi desenvolvido como parte de um desafio proposto por um banco fictício. Ele simula operações reais de uma conta bancária com foco em estrutura modular, uso de boas práticas em Python e experiência do usuário próxima à de um banco digital. 

--- 

## 📌 Funcionalidades 

- ✅ Identificação do cliente via CPF 
- ✅ Criação de novos usuários com CPF único 
- ✅ Abertura de contas bancárias vinculadas a usuários 
- ✅ Depósitos com validação 
- ✅ Saques com limite de valor e quantidade diária 
- ✅ Registro detalhado de extrato com data e hora 
- ✅ Exibição de extrato formatado 
- ✅ Sistema modularizado com funções reutilizáveis 
- ✅ Uso de diferentes tipos de argumentos (posicional, nomeado) 
- ✅ Simulação de sessão única para cliente logado 

--- 

## 🧩 Funções utilizadas 

### 🏦 Funções bancárias 

| Função | Assinatura | Descrição | 
|-------|------------|-----------| 
| `depositar` | `depositar(saldo, valor, extrato, /)` | Realiza depósito com validação. Usa argumentos **posicionais apenas**. | 
| `sacar` | `sacar(*, saldo, valor, extrato, numero_saques)` | Realiza saque com regras. Usa argumentos **keyword-only**. | 
| `mostrar_extrato` | `mostrar_extrato(saldo, /, *, extrato)` | Exibe extrato com saldo atual. Usa **posicional + keyword-only**. | 
| `registrar_operacao` | `registrar_operacao(extrato, tipo, valor)` | Adiciona uma linha de movimentação com data/hora no extrato. | 

### 👤 Funções de usuário e conta 

| Função | Descrição | 
|--------|-----------| 
| `criar_usuario()` | Solicita dados e cadastra novo cliente com CPF único. | 
| `criar_conta(usuario)` | Cria uma conta bancária vinculada ao usuário. | 
| `encontrar_usuario_por_cpf(cpf)` | Busca um cliente na base de usuários pelo CPF. | 
| `encontrar_conta_por_usuario(usuario)` | Busca uma conta vinculada ao usuário. | 
| `listar_contas()` | Mostra todas as contas cadastradas. | 

### 💬 Fluxo do sistema 

| Função | Descrição | 
|--------|-----------| 
| `menu_inicial()` | Fluxo principal. Solicita CPF e conduz ao cadastro ou menu bancário. | 
| `menu_operacoes(usuario, conta)` | Menu de operações após o login, com sessão individual de saldo e extrato. | 

--- 

## 🧠 Conceitos de Python utilizados no projeto 

### 🧩 Modularização e Boas Práticas 

Cada operação foi isolada em uma função clara. Parâmetros foram estruturados com os tipos corretos (posicional, nomeado ou ambos). 

--- 

### ➕ Operadores Aritméticos 

```python 
saldo += valor 
saldo -= valor 
numero_saques += 1 
``` 

--- 

### 🔀 Estruturas Condicionais 

```python 
if valor > saldo: 
    print("Saldo insuficiente") 
elif numero_saques >= LIMITE_SAQUES_DIARIOS: 
    print("Limite atingido") 
``` 

--- 

### 🔁 Estruturas de Repetição 

Dois laços principais: 

- `while True` no menu inicial 
- `while True` no menu do cliente 

--- 

### 🔍 Métodos de String 

```python 
cpf = input(...).strip() 
opcao = input(...).lower().strip() 
``` 

--- 

### 💬 f-Strings e Interpolação 

```python 
print(f"Saldo atual: R$ {saldo:.2f}") 
``` 

--- 

### 🕓 Módulo datetime 

```python 
from datetime import datetime 
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
``` 

--- 

## ✅ Requisitos Técnicos Atendidos 

- [x] Sistema de autenticação via CPF 
- [x] Cadastro único por CPF 
- [x] Abertura de conta com vínculo ao cliente 
- [x] Saques limitados a R$500 e 3 por dia 
- [x] Validações robustas para valores e entradas 
- [x] Registro de operações com data/hora 
- [x] Separação lógica com funções modulares 
- [x] Tipagem avançada de parâmetros de função 

---

## 🧱 Estrutura Orientada a Objetos (POO)

Agora com **programação orientada a objetos (POO)**, baseado em um diagrama UML completo.

### 📦 Classes utilizadas

| Classe         | Descrição |
|----------------|-----------|
| `PessoaFisica` | Representa um cliente pessoa física com CPF, nome e data de nascimento |
| `Cliente`      | Superclasse com lista de contas e endereço |
| `Conta`        | Classe base com saldo, número e histórico de transações |
| `ContaCorrente`| Subclasse com limite de saque e limite diário de saques |
| `Historico`    | Armazena as transações realizadas |
| `Transacao`    | Interface abstrata para `registrar()` uma transação |
| `Saque`        | Implementa `Transacao` para realizar saques |
| `Deposito`     | Implementa `Transacao` para realizar depósitos |

### 🧠 Padrões aplicados

- Encapsulamento com atributos privados
- Herança (`ContaCorrente` herda de `Conta`)
- Polimorfismo com interface `Transacao`
- Composição: `Conta` possui `Historico`
- Métodos de classe (`@classmethod`) e métodos abstratos (`@abstractmethod`)

---

## 🤝 Agradecimentos 

Sou grato ao conteúdo do curso e aos desafios propostos, que permitiram desenvolver não apenas um sistema funcional, mas também a capacidade de pensar como desenvolvedor profissional, com foco em modularidade, clareza e boas práticas. 