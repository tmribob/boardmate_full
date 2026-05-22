from fastapi import APIRouter, Depends, Response, Cookie
from fastapi.security import OAuth2PasswordRequestForm

from app.api.models.auth.login_response import AuthResponse
from app.api.models.auth.register_api import RegisterApi
from app.services.auth_service import AuthService, get_auth_service

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register", status_code=201)
async def register(data: RegisterApi,
                   auth_service: AuthService = Depends(get_auth_service)):
    await auth_service.register_new_user(data.nickname,
                                         data.email,
                                         data.password)


@router.post("/login", status_code=200, response_model=AuthResponse)
async def login(response: Response,
                form_data: OAuth2PasswordRequestForm = Depends(),
                auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.authenticate_user(form_data.username,
                                                form_data.password,
                                                response)


@router.post("/refresh", response_model=AuthResponse)
async def refresh(response: Response,
                  refresh_token: str = Cookie(None),
                  auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.refresh_tokens(refresh_token, response)


@router.post("/logout")
async def logout(response: Response,
                 refresh_token: str = Cookie(None),
                 auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.logout(response, refresh_token)
