from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.user.users_api import UserApi
from app.db.init_db import get_session
from app.enums.friendship_enum import FriendshipStatus
from app.repositories import friend_repo
from app.services.security import get_user_from_token, user_required

router = APIRouter(
    prefix="/friends",
    tags=["friends"]
)


@router.get("/", status_code=200)
async def get_friends(user_uuid: UUID = Depends(get_user_from_token),
                      session: AsyncSession = Depends(get_session)):
    friends = await friend_repo.get_friends(session, user_uuid)

    return [UserApi.model_validate(friend) for friend in friends]


@router.post("/request_friendship", status_code=200, dependencies=[Depends(user_required)])
async def request_friendship(addressee_uuid: UUID,
                             requester_uuid: UUID = Depends(get_user_from_token),
                             session: AsyncSession = Depends(get_session)):
    await friend_repo.request_friendship(session, requester_uuid, addressee_uuid)
    await session.commit()


@router.put("/accept_friendship", status_code=200, dependencies=[Depends(user_required)])
async def accept_friendship(addressee_uuid: UUID,
                            requester_uuid: UUID = Depends(get_user_from_token),
                            session: AsyncSession = Depends(get_session)):
    await friend_repo.update_friendship(session, requester_uuid, addressee_uuid, FriendshipStatus.ACCEPTED)
    await session.commit()


@router.put("/rejected_friendship", status_code=200, dependencies=[Depends(user_required)])
async def rejected_friendship(addressee_uuid: UUID,
                              requester_uuid: UUID = Depends(get_user_from_token),
                              session: AsyncSession = Depends(get_session)):
    await friend_repo.update_friendship(session, requester_uuid, addressee_uuid, FriendshipStatus.REJECTED)
    await session.commit()


@router.get("/incoming_requests", status_code=200, dependencies=[Depends(user_required)])
async def get_incoming_requesters(user_uuid: UUID = Depends(get_user_from_token),
                                  session: AsyncSession = Depends(get_session)):
    requesters = await friend_repo.get_requests(session, user_uuid, "incoming")

    return [UserApi.model_validate(requester) for requester in requesters]


@router.get("/outgoing_requests", status_code=200, dependencies=[Depends(user_required)])
async def get_outgoing_requests(user_uuid: UUID = Depends(get_user_from_token),
                                session: AsyncSession = Depends(get_session)):
    addressees = await friend_repo.get_requests(session, user_uuid, "outgoing")

    return [UserApi.model_validate(addressee) for addressee in addressees]
