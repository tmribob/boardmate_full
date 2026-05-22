from uuid import UUID

from pydantic import BaseModel


class GenreApi(BaseModel):
    uuid: UUID
    name: str
