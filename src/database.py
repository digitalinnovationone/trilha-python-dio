import databases
import sqlalchemy as sa

from src.config import settings

database = databases.Database(settings.database_url)
metadata = sa.MetaData()

if settings.database_url.startswith("sqlite"):
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})
else:
    engine = sa.create_engine(settings.database_url)
