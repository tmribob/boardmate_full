from pydantic import BaseModel, EmailStr, SecretStr


class LoginApi(BaseModel):
    email: EmailStr
    password: SecretStr
