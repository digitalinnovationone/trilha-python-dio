📘 Transactions API — Desafio DIO

API bancária assíncrona construída com FastAPI, seguindo boas práticas de organização em controllers, services, models e schemas, com autenticação via JWT e operações de depósito e saque.

🚀 Tecnologias Utilizadas

Python 3.10+

FastAPI

SQLAlchemy (Core)

Databases (async)

JWT (PyJWT)

Uvicorn

Pydantic

📌 Funcionalidades

✔ Autenticação com JWT
✔ Criar contas
✔ Listar contas do usuário autenticado
✔ Criar transações (depósito e saque)
✔ Validar saldo antes do saque
✔ Listar transações por conta
✔ Banco de dados assíncrono
✔ Estrutura limpa e modular baseada em serviços

📁 Estrutura do Projeto
src/
│
├── controllers/
│   ├── account.py
│   ├── auth.py
│   └── transaction.py
│
├── services/
│   ├── account.py
│   ├── transaction.py
│   └── ...
│
├── models/
│   ├── account.py
│   ├── transaction.py
│
├── schemas/
│   ├── account.py
│   ├── transaction.py
│   └── auth.py
│
├── views/
│   ├── account.py
│   ├── transaction.py
│   └── auth.py
│
├── security.py
├── exceptions.py
├── database.py
└── main.py

🏗️ Como Executar o Projeto
1️⃣ Criar ambiente virtual
python -m venv venv

2️⃣ Ativar ambiente

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar banco e tabelas

O arquivo database.py usa metadata.create_all() ou migrations equivalentes.
Certifique-se de que a conexão está correta.

5️⃣ Rodar servidor
uvicorn main:app --reload


A API ficará disponível em:

➡ http://localhost:8000/docs

➡ http://localhost:8000/openapi.json

🔐 Autenticação

Toda operação (exceto login) requer um token JWT.

🔑 Login

POST /auth/login

Body:

{
  "user_id": 1
}


Resposta:

{
  "access_token": "eyJh..."
}


Use este token no header:

Authorization: Bearer <TOKEN_AQUI>

🧾 Endpoints Principais
🔹 Criar Conta

POST /accounts

{
  "balance": 100.00
}


Resposta:

{
  "id": 1,
  "user_id": 1,
  "balance": 100.0,
  "created_at": "2025-01-01T12:00:00Z"
}

🔹 Listar Contas do Usuário

GET /accounts?limit=10&skip=0

🔹 Extrato da Conta

GET /accounts/{id}/transactions

🔹 Criar Transação

POST /transactions

Corpo para depósito:

{
  "account_id": 1,
  "type": "deposit",
  "amount": 50.00
}


Corpo para saque:

{
  "account_id": 1,
  "type": "withdrawal",
  "amount": 20.00
}


Retorno:

{
  "id": 3,
  "account_id": 1,
  "type": "deposit",
  "amount": 50.0,
  "timestamp": "2025-01-01T12:10:00Z"
}

⚠️ Validações Importantes
❌ Não permite saque acima do saldo

Retorna:

{
  "detail": "Operation not carried out due to lack of balance"
}

❌ Não permite transações em contas de outro usuário
❌ Não aceita valores negativos
🔧 Arquitetura da Solução

O projeto é estruturado em camadas:

Controllers

Recebem requisições HTTP e chamam os services.

Services

Contêm a regra de negócio:

valida saldo

valida conta

processa depósito e saque

verifica se a conta pertence ao usuário autenticado

Models

Mapeamento SQLAlchemy para as tabelas.

Schemas

Entrada (input) e validação Pydantic.

Views

Saída (output) formatada para respostas da API.

Security

JWT + autenticação + autorização.

🧪 Teste Rápido com HTTPie
Login
http POST :8000/auth/login user_id:=1

Criar conta
http POST :8000/accounts Authorization:"Bearer <token>" balance:=50

Fazer depósito
http POST :8000/transactions Authorization:"Bearer <token>" \
    account_id:=1 type=deposit amount:=20

Fazer saque
http POST :8000/transactions Authorization:"Bearer <token>" \
    account_id:=1 type=withdrawal amount:=10

Extrato
http GET :8000/accounts/1/transactions Authorization:"Bearer <token>"

🏁 Conclusão

Essa API cobre todos os requisitos do desafio:

✔ FastAPI assíncrono
✔ JWT com expiração
✔ Estrutura profissional em camadas
✔ Banco e transações
✔ Validações
✔ Segurança
✔ Documentação automática (Swagger)