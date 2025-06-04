# Trilha Python DIO

Este repositório contém os projetos e desafios desenvolvidos durante a trilha de Python oferecida pela Digital Innovation One (DIO).

## Conteúdo

- **Desafios e Projetos**: Implementações em Python abordando diversos temas e frameworks.
- **APIs Assíncronas com FastAPI**: Desenvolvimento de APIs RESTful utilizando o FastAPI.
- **Blog com FastAPI**: Implementação de um blog utilizando o framework FastAPI.

## Desafios

### Desafio: API Bancária Assíncrona com FastAPI

Neste desafio, você irá projetar e implementar uma API RESTful assíncrona usando FastAPI para gerenciar operações bancárias de depósitos e saques, vinculadas a contas correntes.

#### Objetivos e Funcionalidades

- **Cadastro de Transações**: Permita o cadastro de transações bancárias, como depósitos e saques.
- **Exibição de Extrato**: Implemente um endpoint para exibir o extrato de uma conta, mostrando todas as transações realizadas.
- **Autenticação com JWT**: Utilize JWT (JSON Web Tokens) para garantir que apenas usuários autenticados possam acessar os endpoints que exigem autenticação.

#### Requisitos Técnicos

- **FastAPI**: Utilize FastAPI como framework para criar sua API. Aproveite os recursos assíncronos do framework para lidar com operações de I/O de forma eficiente.
- **Modelagem de Dados**: Crie modelos de dados adequados para representar contas correntes e transações. Garanta que as transações estejam relacionadas a uma conta corrente, e que contas possam realizar saques e depósitos de forma segura.
- **Validação das operações**: Não permita depósitos e saques com valores negativos, valide se o usuário possui saldo para realizar o saque.
- **Segurança**: Implemente autenticação usando JWT para proteger os endpoints que necessitam de acesso autenticado.
- **Documentação com OpenAPI**: Certifique-se de que sua API esteja bem documentada, incluindo descrições adequadas para cada endpoint, parâmetros e modelos de dados.

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona uma nova feature'`).
4. Faça um push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato.

---

Aproveite a jornada de aprendizado com Python na DIO!
