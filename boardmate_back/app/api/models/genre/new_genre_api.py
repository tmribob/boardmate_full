from pydantic import BaseModel


class NewGenreApi(BaseModel):
    name: str
