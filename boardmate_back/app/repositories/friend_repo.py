from typing import Sequence, Literal
from uuid import UUID

from sqlalchemy import select, update, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.User.friend_db import FriendDb
from app.db.schemas.User.user_db import UserDb
from app.enums.friendship_enum import FriendshipStatus
from app.repositories.user_repo import get_users


async def get_friends(session: AsyncSession,
                      user_uuid: UUID) -> Sequence[UserDb]:
    query = (
        select(FriendDb)
        .where(
            or_(
                FriendDb.requester_uuid == user_uuid,
                FriendDb.addressee_uuid == user_uuid
            ),
            FriendDb.status == FriendshipStatus.ACCEPTED
        )
    )
    result = await session.execute(query)
    connections = result.scalars().all()

    friend_uuids: set[UUID] = set()
    for conn in connections:
        if conn.requester_uuid == user_uuid:
            friend_uuids.add(conn.addressee_uuid)
        else:
            friend_uuids.add(conn.requester_uuid)

    return await get_users(session, uuids=friend_uuids)


async def get_requests(session: AsyncSession,
                       user_uuid: UUID,
                       direction: Literal["incoming", "outgoing"]) -> Sequence[UserDb]:
    query = select(FriendDb)
    filters = []
    match direction:
        case "incoming":
            filters.append(FriendDb.addressee_uuid == user_uuid)
        case "outgoing":
            filters.append(FriendDb.requester_uuid == user_uuid)
    filters.append(FriendDb.status == FriendshipStatus.PENDING)

    if not filters:
        return []
    query = query.where(and_(*filters))
    result = await session.execute(query)
    uuids: set[UUID] = set()
    match direction:
        case "incoming":
            uuids = {conn.requester_uuid for conn in result.scalars().all()}
        case "outgoing":
            uuids = {conn.addressee_uuid for conn in result.scalars().all()}

    return await get_users(session, uuids=uuids)


async def request_friendship(session: AsyncSession,
                             requester_uuid: UUID,
                             addressee_uuid: UUID):
    new_friendship = FriendDb(requester_uuid=requester_uuid,
                              addressee_uuid=addressee_uuid)
    session.add(new_friendship)


async def update_friendship(session: AsyncSession,
                            requester_uuid: UUID,
                            addressee_uuid: UUID,
                            new_status: FriendshipStatus):
    await session.execute(
        update(FriendDb)
        .where(
            FriendDb.requester_uuid == requester_uuid,
            FriendDb.addressee_uuid == addressee_uuid,
            FriendDb.status == FriendshipStatus.PENDING
        )
        .values(status=new_status)
    )


async def get_friendship_record(session: AsyncSession,
                                user1_uuid: UUID,
                                user2_uuid: UUID) -> FriendDb | None:
    query = select(FriendDb).where(
        or_(
            (FriendDb.requester_uuid == user1_uuid) & (FriendDb.addressee_uuid == user2_uuid),
            (FriendDb.requester_uuid == user2_uuid) & (FriendDb.addressee_uuid == user1_uuid)
        )
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()
