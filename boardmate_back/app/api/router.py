from fastapi import APIRouter

from app.api.routes import games_route, auth_route, users_route, genres_route, difficulties_route, friends_route, seo_route

api_router = APIRouter(
    prefix="/api",
)

api_router.include_router(auth_route.router)
api_router.include_router(seo_route.seo_router)
api_router.include_router(users_route.router)
api_router.include_router(games_route.router)
api_router.include_router(genres_route.router)
api_router.include_router(difficulties_route.router)
api_router.include_router(friends_route.router)
