from typing import Sequence, Set, Optional
from uuid import UUID

from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.User.user_db import UserDb


async def create_user(session: AsyncSession,
                      user_nickname: str) -> UserDb:
    new_user = UserDb(nickname=user_nickname)
    session.add(new_user)
    await session.flush()
    return new_user


async def get_user_by_uuid(session: AsyncSession,
                           user_uuid: UUID) -> UserDb:
    query = select(UserDb).filter_by(uuid=user_uuid)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


async def get_users(session: AsyncSession,
                    nickname: Optional[str] = None,
                    uuids: Optional[Set[UUID]] = None) -> Sequence[UserDb]:
    query = select(UserDb)

    filters = []
    if nickname:
        filters.append(UserDb.nickname.ilike(f"%{nickname}%"))

    if uuids:
        filters.append(UserDb.uuid.in_(uuids))

    if filters:
        query = query.where(and_(*filters))

    result = await session.execute(query)
    return result.scalars().all()


async def update_user(session: AsyncSession,
                      user_uuid: UUID,
                      **values):
    if not values:
        return
    await session.execute(
        update(UserDb)
        .filter_by(uuid=user_uuid)
        .values(**values)
    )
