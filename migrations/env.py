from logging.config import fileConfig

from alembic import context

from src.config import settings

# este é o objeto Alembic Config, que fornece
# acesso aos valores dentro do arquivo .ini em uso.
config = context.config

# Interpretar o arquivo de configuração para o registro em log do Python.
# Esta linha configura os registradores.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


from src.database import engine, metadata  # noqa
from src.models.transaction import transactions  # noqa
from src.models.account import accounts  # noqa

target_metadata = metadata


def run_migrations_offline() -> None:
    """Executa as migrações no modo 'offline'.

    Isto configura o contexto apenas com uma URL
    e não com um Engine, embora um Engine também seja
    aceitável aqui. Ao pular a criação do Engine,
    nem mesmo precisamos que um DBAPI esteja disponível.

    Chamadas para context.execute() aqui emitem a string fornecida
    na saída do script.

    """
    url = settings.database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações no modo 'online'.

    Neste cenário, precisamos criar um Engine
    e associar uma conexão com o contexto.

    """
    connectable = engine

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
