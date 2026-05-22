from uuid import UUID

from pydantic import BaseModel


class FriendshipApi(BaseModel):
    requester_uuid: UUID
    addressee_uuid: UUID
