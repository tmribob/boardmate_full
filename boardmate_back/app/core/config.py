from typing import List

from pydantic import AliasChoices, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SITE_DOMAIN: str = "http://localhost:3000"

    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "boardmate"
    DB_HOST: str = "db"
    DB_PORT: str = "5432"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str = "mysecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    MINIO_ACCESS_KEY: str = "admin"
    MINIO_SECRET_KEY: str = "password"
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_EXTERNAL_URL: str = "http://localhost:9000"
    MINIO_MAX_FILE_SIZE: int = 10 * 1024 * 1024
    MINIO_ALLOWED_TYPES: List[str] = ["image/jpeg", "image/png"]

    DICEBEAR_API_URL: str = "https://api.dicebear.com/7.x/pixel-art/svg"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
