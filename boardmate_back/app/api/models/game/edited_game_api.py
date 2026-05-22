from pydantic import BaseModel


class EditedGameApi(BaseModel):
    name: str
    description: str
    min_players: int
    max_players: int
    min_duration: int
    max_duration: int
