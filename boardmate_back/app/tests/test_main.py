import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_users_profile_rejects_invalid_token(client):
    headers = {"Authorization": "Bearer invalid-token"}
    response = await client.get("/api/users/", headers=headers)
    assert response.status_code == 403


@pytest.mark.integration
@pytest.mark.asyncio
async def test_users_profile_requires_auth(client):
    response = await client.get("/api/users/")
    assert response.status_code == 401


@pytest.mark.integration
@pytest.mark.asyncio
async def test_games_limit_validation(client):
    response = await client.get("/api/games/?limit=101")
    assert response.status_code == 422


@pytest.mark.integration
@pytest.mark.asyncio
async def test_login_requires_credentials(client):
    response = await client.post("/api/auth/login")
    assert response.status_code == 422