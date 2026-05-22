from uuid import UUID

from fastapi import UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.game.edited_game_api import EditedGameApi
from app.api.models.game.new_game_api import NewGameApi
from app.db.init_db import get_session
from app.enums.minio_enum import MinioBuckets
from app.exceptions.NotFoundError import NotFoundError
from app.repositories import game_repo, comment_repo
from app.services.file_service import file_service


async def get_game_service(session: AsyncSession = Depends(get_session)):
    return GameService(session)


class GameService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_new_game(self, data: NewGameApi, photo: UploadFile):
        try:
            new_game = await game_repo.create_game(
                self.session,
                **data.model_dump()
            )
            url = await file_service.upload_game_photo(photo, new_game.uuid)

            await game_repo.edit_game(
                self.session,
                new_game.uuid,
                photo=url
            )
            await self.session.commit()
            return new_game
        except Exception as e:
            await self.session.rollback()
            raise e

    async def get_catalog(self, page: int = 1, limit: int = 20, **filters):
        calculated_offset = (page - 1) * limit
        return await game_repo.get_all_games(self.session,
                                             limit=limit,
                                             offset=calculated_offset,
                                             **filters)

    async def get_detailed_game(self, game_uuid: UUID):
        game = await game_repo.get_game_by_uuid(self.session, game_uuid)
        if not game:
            raise NotFoundError("Игра не найдена")
        return game

    async def update_game_info(self, game_uuid: UUID, update_data: EditedGameApi):
        game = await game_repo.get_game_by_uuid(self.session, game_uuid)
        if not game:
            raise NotFoundError("Игра не найдена")
        safe_data = update_data.model_dump(exclude_unset=True)

        if safe_data:
            await game_repo.edit_game(self.session, game_uuid, **safe_data)
            await self.session.commit()
        await self.session.refresh(game)
        return game

    async def delete_game_with_files(self, game_uuid: UUID):
        try:
            await file_service.cleanup_entity_data(game_uuid, MinioBuckets.GAMES_PHOTOS)
            await game_repo.delete_game(self.session, game_uuid)

            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e

    async def leave_comment(self, game_uuid: UUID, user_uuid: UUID, text: str):
        await self.get_detailed_game(game_uuid)

        await comment_repo.create_comment(
            self.session,
            context=text,
            user_uuid=user_uuid,
            game_uuid=game_uuid
        )
        await self.session.commit()

    async def get_comments(self, game_uuid: UUID):
        await self.get_detailed_game(game_uuid)

        return await comment_repo.get_comments(self.session, game_uuid)

    async def set_rate(self, game_uuid: UUID, user_uuid: UUID, rate: int):
        game = await game_repo.get_game_by_uuid(self.session, game_uuid)
        if not game:
            raise NotFoundError("Игра не найдена")

        await game_repo.rate_game_by_user(
            self.session,
            rate=rate,
            user_uuid=user_uuid,
            game_uuid=game_uuid
        )
        await self.session.commit()

    async def toggle_like(self, game_uuid: UUID, user_uuid: UUID):
        game = await self.get_detailed_game(game_uuid)

        is_liked = any(like.user_uuid == user_uuid for like in game.users)

        if is_liked:
            await game_repo.delete_like_by_user(self.session, user_uuid, game_uuid)
            status = "unliked"
        else:
            await game_repo.like_game_by_user(self.session, user_uuid, game_uuid)
            status = "liked"

        await self.session.commit()
        return status
