from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class UserApi(BaseModel):
    uuid: UUID
    nickname: str = Field(..., min_length=4, max_length=32, description="4-32")
    description: Optional[str] = ''
    avatar: str
