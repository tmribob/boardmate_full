from pydantic import BaseModel, EmailStr, SecretStr, Field


class RegisterApi(BaseModel):
    email: EmailStr
    nickname: str = Field(..., min_length=4, max_length=32, description="4-32")
    password: SecretStr
