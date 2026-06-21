# Trilha Python DIO
## Sistema Bancário Otimizado com Python (POO)

Este projeto consiste na reformulação completa de um sistema bancário básico, migrando uma estrutura sequencial/funcional para o paradigma de **Programação Orientada a Objetos (POO)** em Python. O desafio faz parte do Bootcamp da Digital Innovation One (DIO).

## Tecnologias e Conceitos Aplicados

* **Python 3**: Linguagem base utilizada.
* **Classes e Objetos**: Estruturação de entidades do mundo real como `Cliente`, `PessoaFisica`, `Conta` e `ContaCorrente`.
* **Herança e Polimorfismo**: Reaproveitamento e extensão da classe base `Conta` para criar uma `ContaCorrente` com regras específicas de limite.
* **Classes Abstratas (ABC)**: Implementação da classe `Transacao` utilizando o decorador `@abstractmethod`.
* **Encapsulamento**: Proteção de atributos críticos (como saldo e histórico) utilizando propriedades (`@property`).
* **Tratamento de Exceções**: Uso de blocos `try/except` com `ValueError` para evitar travamentos caso o usuário digite letras no lugar de números nos campos de valores.

## Funcionalidades Cadastrada

* **Cadastro de Clientes**: Criação de usuários do tipo Pessoa Física com validação para impedir CPFs duplicados.
* **Vínculo de Contas**: Abertura automática de contas correntes vinculadas ao CPF do cliente.
