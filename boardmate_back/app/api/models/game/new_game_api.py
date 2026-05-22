from typing import List

from pydantic import BaseModel


class NewGameApi(BaseModel):
    name: str
    genres: List[str]
    difficulty: str
    description: str
    min_players: int
    max_players: int
    min_duration: int
    max_duration: int
