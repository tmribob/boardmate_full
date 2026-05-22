from uuid import UUID

from fastapi import UploadFile, HTTPException
from minio import Minio

from app.core.config import settings
from app.enums.minio_enum import MinioBuckets

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False,
)


async def upload_file_to_minio(file: UploadFile,
                               entity_id: UUID,
                               bucket_name: MinioBuckets) -> str:

    safe_filename = file.filename.replace(" ", "_")
    object_name = f"{entity_id}/{safe_filename}"
    try:
        client.put_object(
            bucket_name.value,
            object_name,
            file.file,
            length=-1,
            part_size=5 * 1024 * 1024,
            content_type=file.content_type
        )
        return f"{settings.MINIO_EXTERNAL_URL}/{bucket_name}/{object_name}"

    except Exception as e:
        print(f"Критическая ошибка MinIO: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при сохранении файла в хранилище")


async def delete_entity_directory(entity_id: UUID, bucket_name: MinioBuckets):
    try:
        prefix = f"{entity_id}/"
        objects_to_delete = client.list_objects(bucket_name.value, prefix=prefix, recursive=True)

        for obj in objects_to_delete:
            client.remove_object(bucket_name.value, obj.object_name)

    except Exception as e:
        print(f"Ошибка при очистке директории {entity_id}: {e}")
