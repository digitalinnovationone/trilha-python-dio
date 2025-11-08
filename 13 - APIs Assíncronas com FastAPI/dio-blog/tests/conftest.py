import asyncio

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from src.config import settings

settings.database_url = "sqlite:///tests.db"


@pytest_asyncio.fixture
async def db(request):
    from src.database import database, engine, metadata  # noqa
    from src.models.post import posts  # noqa

    await database.connect()
    metadata.create_all(engine)

    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine)

        asyncio.run(_teardown())

    request.addfinalizer(teardown)


@pytest_asyncio.fixture
async def client(db):
    from src.main import app

    transport = ASGITransport(app=app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    async with AsyncClient(base_url="http://test", transport=transport, headers=headers) as client:
        yield client


@pytest_asyncio.fixture
async def access_token(client: AsyncClient):
    response = await client.post("/auth/login", json={"user_id": 1})
    return response.json()["access_token"]
