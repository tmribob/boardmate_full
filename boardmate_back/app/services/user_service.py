from typing import Sequence
from uuid import UUID

from fastapi import UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.init_db import get_session
from app.db.schemas.User.user_db import UserDb
from app.enums.roles_enum import Roles
from app.exceptions.NotFoundError import NotFoundError
from app.repositories import user_repo
from app.services.file_service import file_service
from app.core.config import settings


async def get_user_service(session: AsyncSession = Depends(get_session)):
    return UserService(session)


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_profile(self, user_uuid: UUID) -> UserDb:
        user = await user_repo.get_user_by_uuid(self.session, user_uuid)
        if not user:
            raise NotFoundError("Пользователь не найден")
        user.avatar = self._get_avatar_url(user)
        return user

    @staticmethod
    def _get_avatar_url(user: UserDb) -> str:
        avatar_path: str | None = user.avatar
        if avatar_path:
            return avatar_path

        return f"https://api.dicebear.com/7.x/pixel-art/svg?seed={user.uuid}"

    async def update_profile(self, user_uuid: UUID, nickname: str, description: str, avatar: UploadFile | None):
        user = await user_repo.get_user_by_uuid(self.session, user_uuid)

        if not user:
            raise NotFoundError("Пользователь не найден")

        update_data = {"nickname": nickname, "description": description}
        if avatar and avatar.filename:

            url = await file_service.upload_user_avatar(avatar, user_uuid)
            update_data["avatar"] = url

        if update_data:
            await user_repo.update_user(self.session, user_uuid, **update_data)
            await self.session.commit()
            await self.session.refresh(user)
        return user

    async def change_user_role(self, user_uuid: UUID, to_admin: bool):
        roles = [Roles.USER, Roles.ADMIN] if to_admin else [Roles.USER]
        await user_repo.update_user(self.session, user_uuid, roles=roles)
        await self.session.commit()

    async def get_all_users(self) -> Sequence[UserDb]:
        return await user_repo.get_users(self.session)

    async def get_user_json_ld(self, user: UserDb):
        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": user.nickname,
            "description": user.description,
            "image": user.avatar,
            "url": f"{settings.SITE_DOMAIN}/users/{user.uuid}"
        }
