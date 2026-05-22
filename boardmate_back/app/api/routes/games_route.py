import json
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, Query, Form, File

from app.api.models.game.edited_game_api import EditedGameApi
from app.api.models.game.game_api import GameApi
from app.api.models.game.new_game_api import NewGameApi
from app.services.game_service import GameService, get_game_service
from app.services.security import get_user_from_token, admin_required, user_required

router = APIRouter(
    prefix="/games",
    tags=["games"]
)


@router.get("/", status_code=200)
async def get_games(search: Optional[str] = None,
                    player_count: Optional[int] = None,
                    duration: Optional[int] = None,
                    genre_uuids: Optional[List[UUID]] = Query(None),
                    difficulty_uuid: Optional[UUID] = None,
                    limit: int = Query(20, le=100),
                    page: int = Query(1, ge=1),
                    sort_by: str = "name",
                    order: str = "asc",
                    game_service: GameService = Depends(get_game_service)):
    games = await game_service.get_catalog(page=page,
                                           limit=limit,
                                           search=search,
                                           player_count=player_count,
                                           duration=duration,
                                           genre_uuids=genre_uuids,
                                           difficulty_uuid=difficulty_uuid,
                                           sort_by=sort_by,
                                           order=order)
    return [GameApi.model_validate(game) for game in games]


@router.post("/", status_code=200, dependencies=[Depends(admin_required)])
async def create_game(data: str = Form(...),
                      photo: UploadFile | None = File(None),
                      game_service: GameService = Depends(get_game_service)):
    game_data = NewGameApi.model_validate(json.loads(data))
    await game_service.create_new_game(game_data, photo)


@router.delete("/{game_uuid}", status_code=200, dependencies=[Depends(admin_required)])
async def delete_game(game_uuid: UUID,
                      game_service: GameService = Depends(get_game_service)):
    await game_service.delete_game_with_files(game_uuid)


@router.get("/{game_uuid}", status_code=200)
async def get_game(game_uuid: UUID,
                   game_service: GameService = Depends(get_game_service)):
    game = await game_service.get_detailed_game(game_uuid)
    return GameApi.model_validate(game)


@router.put("/{game_uuid}", status_code=200, dependencies=[Depends(admin_required)])
async def edit(data: EditedGameApi,
               game_uuid: UUID,
               game_service: GameService = Depends(get_game_service)):
    return await game_service.update_game_info(game_uuid, data)


@router.post("/{game_uuid}/comment", status_code=200, dependencies=[Depends(user_required)])
async def create_comment(text: str,
                         game_uuid: UUID,
                         user_uuid: UUID = Depends(get_user_from_token),
                         game_service: GameService = Depends(get_game_service)):
    await game_service.leave_comment(user_uuid=user_uuid, game_uuid=game_uuid, text=text)


@router.get("/{game_uuid}/comment", status_code=200)
async def get_comments(game_uuid: UUID,
                       game_service: GameService = Depends(get_game_service)):
    await game_service.get_comments(game_uuid)


@router.post("/{game_uuid}/rate", status_code=200, dependencies=[Depends(user_required)])
async def rate_game(rate: int,
                    game_uuid: UUID,
                    user_uuid: UUID = Depends(get_user_from_token),
                    game_service: GameService = Depends(get_game_service)):
    await game_service.set_rate(game_uuid=game_uuid, user_uuid=user_uuid, rate=rate)


@router.post("/{game_uuid}/like", status_code=200, dependencies=[Depends(user_required)])
async def like(game_uuid: UUID,
               user_uuid: UUID = Depends(get_user_from_token),
               game_service: GameService = Depends(get_game_service)):
    await game_service.toggle_like(user_uuid=user_uuid, game_uuid=game_uuid)
