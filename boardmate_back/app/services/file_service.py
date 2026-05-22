from uuid import UUID

from fastapi import UploadFile, HTTPException

from app.core.config import settings
from app.enums.minio_enum import MinioBuckets
from app.repositories import minio_repo


class FileService:
    @staticmethod
    async def _validate_file(file: UploadFile):
        if file.content_type not in settings.MINIO_ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Тип {file.content_type} не поддерживается. Разрешены: {settings.MINIO_ALLOWED_TYPES}"
            )
        size = file.size if file.size else 0
        if size > settings.MINIO_MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="Файл слишком большой")

    async def upload_user_avatar(self, file: UploadFile, user_uuid: UUID) -> str:
        await self._validate_file(file)
        await self.cleanup_entity_data(user_uuid, MinioBuckets.USERS_AVATARS)
        extension = file.filename.split('.')[-1] if '.' in file.filename else 'png'
        file.filename = f"main.{extension}"

        return await minio_repo.upload_file_to_minio(
            file, user_uuid, MinioBuckets.USERS_AVATARS
        )

    async def upload_game_photo(self, file: UploadFile, game_uuid: UUID) -> str:
        await self._validate_file(file)
        return await minio_repo.upload_file_to_minio(
            file, game_uuid, MinioBuckets.GAMES_PHOTOS
        )

    async def cleanup_entity_data(self, entity_id: UUID, bucket: MinioBuckets):
        await minio_repo.delete_entity_directory(entity_id, bucket)


file_service = FileService()
