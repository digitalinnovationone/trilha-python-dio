# FastAPI Banking (Assíncrono)


API RESTful assíncrona para operações bancárias (depósitos/saques) com autenticação JWT.


## Funcionalidades


- Cadastro de transações (depósito/saque)
- Extrato por conta
- Autenticação com JWT
- Validações: valores negativos e saldo para saque
- Documentação automática via OpenAPI/Swagger


## Como rodar (local)


1. Copie `.env.example` para `.env` e ajuste as variáveis.
2. Instale dependências (usando poetry):


```bash
poetry install --no-root --without dev
