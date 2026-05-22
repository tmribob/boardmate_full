from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.User.user_auth_db import UserAuthDb


async def create_user_auth(session: AsyncSession,
                           user_email: str,
                           user_password: str,
                           user_uuid: UUID):
    new_auth = UserAuthDb(
        email=user_email,
        password=user_password,
        user_uuid=user_uuid
    )
    session.add(new_auth)


async def get_user_by_email(session: AsyncSession,
                            user_email: str) -> UserAuthDb | None:
    query = (
        select(UserAuthDb)
        .filter_by(email=user_email)
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_user_auth_by_uuid(session: AsyncSession,
                                user_uuid: UUID) -> UserAuthDb:
    query = select(UserAuthDb).filter_by(uuid=user_uuid)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


async def update_refresh_token(session: AsyncSession,
                               user_uuid: UUID,
                               new_token: str | None):
    await session.execute(
        update(UserAuthDb)
        .filter_by(uuid=user_uuid)
        .values(current_refresh=new_token)
    )
