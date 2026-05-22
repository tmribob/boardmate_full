from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from app.services.file_service import FileService


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_file_rejects_unsupported_type():
    file = SimpleNamespace(content_type="text/plain", size=128)

    with pytest.raises(HTTPException) as exc_info:
        await FileService._validate_file(file)

    assert exc_info.value.status_code == 400


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_file_rejects_too_large_file(monkeypatch):
    monkeypatch.setattr("app.services.file_service.settings.MINIO_MAX_FILE_SIZE", 5)
    file = SimpleNamespace(content_type="image/png", size=6)

    with pytest.raises(HTTPException) as exc_info:
        await FileService._validate_file(file)

    assert exc_info.value.status_code == 413


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_file_accepts_supported_file(monkeypatch):
    monkeypatch.setattr("app.services.file_service.settings.MINIO_MAX_FILE_SIZE", 10)
    file = SimpleNamespace(content_type="image/png", size=10)

    await FileService._validate_file(file)
