from uuid import uuid4

import pytest
from fastapi import Response

from app.api.models.auth.login_response import AuthResponse
from app.services.auth_service import AuthService


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_authenticate_user_happy_path(monkeypatch):
    expected_uuid = uuid4()

    class FakeUserAuth:
        def __init__(self):
            self.password = "hashed"
            self.user_uuid = expected_uuid

    async def fake_get_user_by_email(_session, _email):
        return FakeUserAuth()

    async def fake_get_auth_response(self, _response, user_uuid):
        return AuthResponse(access_token=f"token-for-{user_uuid}", token_type="bearer")

    monkeypatch.setattr("app.services.auth_service.auth_repo.get_user_by_email", fake_get_user_by_email)
    monkeypatch.setattr("app.services.auth_service.security.verify_password", lambda plain, hashed: True)
    monkeypatch.setattr("app.services.auth_service.AuthService._AuthService__get_auth_response", fake_get_auth_response)

    service = AuthService(session=object())
    response = await service.authenticate_user(
        email="test@mail.com",
        password="strong-pass",
        response=Response(),
    )

    assert response.token_type == "bearer"
    assert str(expected_uuid) in response.access_token
