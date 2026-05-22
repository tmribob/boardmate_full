from typing import Optional

from pydantic import BaseModel, Field


class EditedUserApi(BaseModel):
    nickname: str = Field(..., min_length=4, max_length=32, description="4-32")
    description: Optional[str] = None
