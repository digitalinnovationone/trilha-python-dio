# 📌 Sistema Bancário em Python — Bootcamp Luizalabs Back-end com Python (DIO)

Este projeto foi desenvolvido como parte do **primeiro desafio do Bootcamp Luizalabs Back-end com Python**, oferecido pela Digital Innovation One (DIO).  
O objetivo principal foi evoluir o sistema bancário inicialmente proposto, tornando-o **modularizado**, mais organizado e capaz de realizar o **cadastro de usuários e contas bancárias**.

---

## 🎯 Objetivos do Desafio

### ✔ Modularização completa do código  
As operações foram separadas em funções, respeitando regras específicas sobre como os argumentos devem ser recebidos:
- **Depósito** → argumentos *positional-only*
- **Saque** → argumentos *keyword-only*
- **Extrato** → combinação de *positional-only* e *keyword-only*

### ✔ Novas funcionalidades implementadas  
Além das operações de saque, depósito e extrato, o sistema agora inclui:

- **Cadastro de Usuários**  
  - Nome  
  - Data de nascimento  
  - CPF (somente números, não pode repetir)  
  - Endereço completo  

- **Cadastro de Contas Correntes**  
  - Agência padrão: `0001`  
  - Número da conta sequencial  
  - Uma conta pertence a um usuário; um usuário pode ter várias contas  

- **Listagem de contas existentes**  

----

## 🧠 O que aprendi neste desafio

- Organização do código usando funções
- Uso de *positional-only* (`/`) e *keyword-only* (`*`) no Python
- Estruturação de dados com listas e dicionários
- Boas práticas de modularização
- Criação de múltiplos fluxos no menu principal
- Operações bancárias simuladas (saque, depósito, extrato)
- Validação de CPF e controle de múltiplas contas
- Fluxo completo de Git:
  - Fork → Clone → Branch → Commit → Push → Pull Request

----

## 🏗 Estrutura do Projeto
trilha-python-dio/
└── 00 - Fundamentos/
└── desafio.py


O código final refatorado se encontra no arquivo **`desafio.py`** dentro da pasta *"00 - Fundamentos"*.

---

## 🚀 Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/lexsantana/trilha-python-dio


## Entre na pasta
cd trilha-python-dio

## Execute o script
python "00 - Fundamentos/desafio.py"

## 📚 Tecnologias

- Python 3
- Git / GitHub
- VS Code

## ✨ Sobre mim

💼 Alexsander, graduado em Engenharia Aeronáutica e Mecânica, com pós-graduação em Engenharia Submarina pela Universidade Petrobras
💻 Estudante de Python e entusiasta de IA
📈 Construindo portfólio para área de tecnologia

** Nov 18 2025
