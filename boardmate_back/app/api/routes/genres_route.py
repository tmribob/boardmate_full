from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.genre.genre_api import GenreApi
from app.api.models.genre.new_genre_api import NewGenreApi
from app.db.init_db import get_session
from app.repositories import genre_repo
from app.services.security import admin_required

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)


@router.get("/", status_code=200)
async def get_genres(session: AsyncSession = Depends(get_session)):
    genres = await genre_repo.get_genres(session)

    return [GenreApi.model_validate(genre) for genre in genres]


@router.post("/", status_code=200, dependencies=[Depends(admin_required)])
async def create_genre(data: NewGenreApi,
                       session: AsyncSession = Depends(get_session)):
    await genre_repo.create_genre(session, data)
    await session.commit()
