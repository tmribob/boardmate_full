from pydantic import BaseModel


class DifficultyApi(BaseModel):
    name: str
