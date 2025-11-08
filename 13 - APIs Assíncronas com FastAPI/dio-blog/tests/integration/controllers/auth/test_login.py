from fastapi import status
from httpx import AsyncClient


async def test_login_success(client: AsyncClient):
    # Given
    data = {"user_id": 1}

    # When
    response = await client.post("/auth/login", json=data)

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["access_token"] is not None
