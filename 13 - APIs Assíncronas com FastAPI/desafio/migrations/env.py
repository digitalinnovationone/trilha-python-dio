from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from src.config import settings
from src.database import metadata
import src.models.account  # noqa: F401
import src.models.transaction  # noqa: F401

# Alembic Config object, which provides access to the values
# within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = metadata


def get_context_config() -> dict:
    return {
        "target_metadata": target_metadata,
        "compare_type": True,
        "compare_server_default": True,
        "render_as_batch": settings.database_url.startswith("sqlite"),
    }


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=settings.database_url,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        **get_context_config(),
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(settings.database_url)

    with connectable.connect() as connection:
        context.configure(connection=connection, **get_context_config())

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
