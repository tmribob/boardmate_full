from typing import List
from uuid import UUID

from pydantic import BaseModel

from app.api.models.comment.comment_api import CommentApi


class GameApi(BaseModel):
    uuid: UUID
    name: str
    description: str
    followers: int
    rate: float
    photo: str
    min_players: int
    max_players: int
    min_duration: int
    max_duration: int
    comments: List[CommentApi]
