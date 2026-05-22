from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.genre.new_genre_api import NewGenreApi
from app.db.schemas.Game.genre_db import GenreDb


async def get_genres(session: AsyncSession) -> Sequence[GenreDb]:
    query = select(GenreDb)
    result = await session.execute(query)
    return result.scalars().all()


async def create_genre(session: AsyncSession,
                       data: NewGenreApi):
    new_genre = GenreDb(name=data.name)
    session.add(new_genre)
