import datetime
from typing import Dict

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from werkzeug.security import generate_password_hash, check_password_hash

from app.db.schemas.User.user_db import UserDb
from app.enums.roles_enum import Roles
from app.enums.tokens_enum import TokensTypes
from app.exceptions.InvalidTokenError import InvalidTokenError
from app.repositories.user_repo import get_user_by_uuid
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_token(data: Dict, token_type: TokensTypes):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.UTC)
    match token_type:
        case TokensTypes.ACCESS:
            expire += datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        case TokensTypes.REFRESH:
            expire += datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": token_type.value})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def verify_password(plain_password: str,
                    hashed_password: str) -> bool:
    return check_password_hash(hashed_password,
                               plain_password)


def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise InvalidTokenError("The token has expired")
    except jwt.InvalidTokenError:
        raise InvalidTokenError("Invalid token")


def get_user_from_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "refresh":
            raise InvalidTokenError("Invalid refresh token type")
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise InvalidTokenError("Refresh token has expired")
    except jwt.InvalidTokenError:
        raise InvalidTokenError("Invalid refresh token")


def role_checker(allowed_role: Roles):
    def checker(current_user: UserDb = Depends(get_user_by_uuid)):
        if allowed_role not in current_user.roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Недостаточно прав. Требуется роль: {allowed_role.value}",
            )
        return current_user

    return checker


def admin_required():
    return role_checker(Roles.ADMIN)


def user_required():
    return role_checker(Roles.USER)
