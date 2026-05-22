from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.difficulty.difficulty_api import DifficultyApi
from app.db.init_db import get_session
from app.repositories import difficulty_repo
from app.services.security import admin_required

router = APIRouter(
    prefix="/difficulty",
    tags=["difficulty"]
)


@router.get("/", status_code=200)
async def get_difficulties(session: AsyncSession = Depends(get_session)):
    difficulties = await difficulty_repo.get_difficulties(session)

    return [DifficultyApi.model_validate(difficulty) for difficulty in difficulties]


@router.post("/", status_code=200, dependencies=[Depends(admin_required)])
async def create_difficulty(data: DifficultyApi,
                            session: AsyncSession = Depends(get_session)):
    await difficulty_repo.create_difficulty(session, data)
    await session.commit()
