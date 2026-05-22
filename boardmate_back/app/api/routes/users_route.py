from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.models.user.edited_user_api import EditedUserApi
from app.api.models.user.users_api import UserApi
from app.services.security import get_user_from_token, user_required, admin_required
from app.services.user_service import UserService, get_user_service

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
templates = Jinja2Templates(directory="templates")


@router.get("/", status_code=200)
async def get_user(user_uuid: UUID = Depends(get_user_from_token),
                   service: UserService = Depends(get_user_service)):
    user = await service.get_user_profile(user_uuid)
    return UserApi.model_validate(user)


@router.get("/users/{user_uuid}", response_class=HTMLResponse)
async def read_user_page(request: Request,
                         user_uuid: UUID,
                         service: UserService = Depends(get_user_service)):
    user = await service.get_user_profile(user_uuid)
    json_ld = service.get_user_json_ld(user)

    return templates.TemplateResponse("user_profile.html", {
        "request": request,
        "user": user,
        "json_ld": json_ld
    })


@router.put("/edit", status_code=200, dependencies=[Depends(user_required)])
async def edit(data: EditedUserApi,
               avatar: UploadFile,
               user_uuid: UUID = Depends(get_user_from_token),
               service: UserService = Depends(get_user_service)):
    await service.update_profile(user_uuid, nickname=data.nickname, description=data.description, avatar=avatar)


@router.put("/promotion", status_code=200, dependencies=[Depends(admin_required)])
async def promotion(user_uuid: UUID,
                    service: UserService = Depends(get_user_service)):
    await service.change_user_role(user_uuid, to_admin=True)


@router.put("/demote", status_code=200, dependencies=[Depends(admin_required)])
async def demote(user_uuid: UUID,
                 service: UserService = Depends(get_user_service)):
    await service.change_user_role(user_uuid, to_admin=False)
