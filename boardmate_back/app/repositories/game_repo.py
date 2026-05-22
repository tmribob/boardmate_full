from typing import Sequence, Optional, List
from uuid import UUID

from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from app.db.schemas.Game.game_db import GameDb
from app.db.schemas.Game.game_genre_db import GameGenreDb
from app.db.schemas.comment_db import CommentDb
from app.db.schemas.like_dp import LikeDb
from app.db.schemas.rate_db import RateDb


async def get_all_games(session: AsyncSession,
                        search: Optional[str] = None,
                        player_count: Optional[int] = None,
                        duration: Optional[int] = None,
                        genre_uuids: Optional[List[UUID]] = None,
                        difficulty_uuid: Optional[UUID] = None,
                        limit: int = 20,
                        offset: int = 0,
                        sort_by: str = "name",
                        order: str = "asc") -> Sequence[GameDb]:
    query = (
        select(GameDb)
        .options(
            joinedload(GameDb.difficulty)
        )
    )

    filters = []
    if search:
        filters.append(GameDb.name.ilike(f"%{search}%"))

    if player_count:
        filters.append(and_(
            GameDb.min_players <= player_count,
            GameDb.max_players >= player_count
        ))

    if duration:
        filters.append(and_(
            GameDb.min_duration <= duration,
            GameDb.max_duration >= duration
        ))

    if difficulty_uuid:
        filters.append(GameDb.difficulty_uuid == difficulty_uuid)

    if filters:
        query = query.where(and_(*filters))

    if genre_uuids:
        query = query.join(GameDb.genres).where(GameGenreDb.genre_uuid.in_(genre_uuids))

    sort_attr = getattr(GameDb, sort_by, GameDb.name)
    query = query.order_by(sort_attr.desc() if order == "desc" else sort_attr.asc())
    query = query.distinct().limit(limit).offset(offset)

    result = await session.execute(query)
    return result.scalars().all()


async def get_game_by_uuid(session: AsyncSession,
                           game_uuid: UUID) -> GameDb | None:
    query = (
        select(GameDb)
        .filter_by(uuid=game_uuid)
        .options(
            joinedload(GameDb.difficulty),
            selectinload(GameDb.genres).joinedload(GameGenreDb.genre),
            selectinload(GameDb.comments),
            selectinload(GameDb.users)
        )
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def create_game(session: AsyncSession,
                      **values) -> GameDb:
    new_game = GameDb(**values)
    session.add(new_game)
    await session.flush()
    return new_game


async def edit_game(session: AsyncSession,
                    game_uuid: UUID,
                    **values):
    if not values:
        return
    await session.execute(
        update(GameDb)
        .filter_by(uuid=game_uuid)
        .values(**values)
    )


async def delete_game(session: AsyncSession, game_uuid: UUID):
    await session.execute(delete(GameDb).where(GameDb.uuid == game_uuid))


async def create_comment_by_user(session: AsyncSession,
                                 context: str,
                                 user_uuid: UUID,
                                 game_uuid: UUID):
    new_comment = CommentDb(context=context,
                            game_uuid=game_uuid,
                            user_uuid=user_uuid)
    session.add(new_comment)


async def rate_game_by_user(session: AsyncSession,
                            rate: int,
                            user_uuid: UUID,
                            game_uuid: UUID):
    new_rate = RateDb(rate=rate,
                      game_uuid=game_uuid,
                      user_uuid=user_uuid)
    session.add(new_rate)


async def like_game_by_user(session: AsyncSession,
                            user_uuid: UUID,
                            game_uuid: UUID):
    new_rate = LikeDb(game_uuid=game_uuid,
                      user_uuid=user_uuid)
    session.add(new_rate)


async def delete_like_by_user(session: AsyncSession,
                              user_uuid: UUID,
                              game_uuid: UUID):
    await session.execute(
        delete(LikeDb).where(
            LikeDb.user_uuid == user_uuid,
            LikeDb.game_uuid == game_uuid
        )
    )
