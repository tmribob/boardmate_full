from uuid import UUID

from fastapi import Depends, Response
from pydantic import SecretStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.auth.login_response import AuthResponse
from app.db.init_db import get_session
from app.enums.tokens_enum import TokensTypes
from app.exceptions.DuplicatedEntryError import DuplicatedEntryError
from app.exceptions.InvalidTokenError import InvalidTokenError
from app.exceptions.NoEntryError import NoEntryError
from app.repositories import user_repo, auth_repo
from app.services import security


async def get_auth_service(session: AsyncSession = Depends(get_session)):
    return AuthService(session)


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_new_user(self,
                                nickname: str,
                                email: str,
                                password: SecretStr):
        hashed_pw = security.hash_password(password.get_secret_value())
        try:
            new_user = await user_repo.create_user(self.session, nickname)
            await auth_repo.create_user_auth(self.session, email, hashed_pw, new_user.uuid)
            await self.session.commit()
            await self.session.refresh(new_user)
        except IntegrityError:
            await self.session.rollback()
            raise DuplicatedEntryError("User with this email or nickname already exists")
        except Exception:
            await self.session.rollback()
            raise

    async def authenticate_user(self,
                                email: str,
                                password: str,
                                response: Response) -> AuthResponse:
        user = await auth_repo.get_user_by_email(self.session, email)

        if not user or not security.verify_password(password, user.password):
            raise NoEntryError("Invalid email or password")

        return await self.__get_auth_response(response, user.user_uuid)

    async def logout(self,
                     response: Response,
                     refresh_token: str):
        user_uuid = security.get_user_from_refresh_token(refresh_token)

        try:
            await auth_repo.update_refresh_token(self.session, user_uuid, None)
            await self.session.commit()
            response.delete_cookie(key="refresh_token",
                                   httponly=True,
                                   samesite="lax")
            return {"detail": "Session successful"}
        except Exception:
            await self.session.rollback()
            raise

    async def refresh_tokens(self,
                             refresh_token: str,
                             response: Response) -> AuthResponse:
        user_uuid = security.get_user_from_refresh_token(refresh_token)
        user = await auth_repo.get_user_auth_by_uuid(self.session, user_uuid)

        if not user or user.current_refresh != refresh_token:
            raise InvalidTokenError("User not found")

        return await self.__get_auth_response(response, user.user_uuid)

    async def __get_auth_response(self,
                                  response: Response,
                                  user_uuid: UUID) -> AuthResponse:
        access_token = security.create_token({"sub": user_uuid}, TokensTypes.ACCESS)
        refresh_token = security.create_token({"sub": user_uuid}, TokensTypes.REFRESH)

        try:
            await auth_repo.update_refresh_token(self.session, user_uuid, refresh_token)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        await self.__set_refresh_cookie(response, refresh_token)

        return AuthResponse(
            access_token=access_token,
            token_type="bearer"
        )

    @staticmethod
    async def __set_refresh_cookie(response: Response,
                                   token: str):
        response.set_cookie(key="refresh_token",
                            value=token,
                            httponly=True,
                            secure=False,
                            samesite="lax",
                            max_age=60 * 60 * 24 * 7)
