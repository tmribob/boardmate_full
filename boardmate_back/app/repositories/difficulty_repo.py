from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.difficulty.difficulty_api import DifficultyApi
from app.db.schemas.Game.difficulty_db import DifficultyDb


async def get_difficulties(session: AsyncSession) -> Sequence[DifficultyDb]:
    query = select(DifficultyDb)
    result = await session.execute(query)
    return result.scalars().all()


async def create_difficulty(session: AsyncSession,
                            data: DifficultyApi):
    new_difficulty = DifficultyDb(name=data.name)
    session.add(new_difficulty)
