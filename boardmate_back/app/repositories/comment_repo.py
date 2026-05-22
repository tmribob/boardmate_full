from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.db.schemas.comment_db import CommentDb


async def get_comments(session: AsyncSession,
                       game_uuid: UUID) -> Sequence[CommentDb]:
    query = (select(CommentDb)
             .filter_by(game_uuid=game_uuid)
             .options(joinedload(CommentDb.user)))
    result = await session.execute(query)
    return result.scalars().all()


async def create_comment(session: AsyncSession,
                         context: str,
                         user_uuid: UUID,
                         game_uuid: UUID):
    new_comment = CommentDb(context=context,
                            game_uuid=game_uuid,
                            user_uuid=user_uuid)
    session.add(new_comment)
