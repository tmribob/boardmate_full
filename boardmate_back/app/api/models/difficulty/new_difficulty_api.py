from pydantic import BaseModel


class NewDifficultyApi(BaseModel):
    name: str
