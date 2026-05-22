from uuid import UUID

from pydantic import BaseModel


class CommentApi(BaseModel):
    user_uuid: UUID
    context: str
    game_uuid: UUID
    count_likes: int
