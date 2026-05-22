from fastapi import APIRouter, Response, Depends

from app.core.config import settings
from app.services.game_service import GameService, get_game_service
from app.services.user_service import UserService, get_user_service

seo_router = APIRouter(tags=["SEO"])


@seo_router.get("/robots.txt", response_class=Response)
async def get_robots_txt():
    lines = [
        "User-agent: *",
        "Allow: /",
        "Allow: /games/",
        "Allow: /users/",
        "Disallow: /admin/",
        "Disallow: /auth/",
        "Disallow: /api/",
        "",
        f"Sitemap: {settings.SITE_DOMAIN}/sitemap.xml"
    ]
    content = "\n".join(lines)
    return Response(content=content, media_type="text/plain")


@seo_router.get("/sitemap.xml", response_class=Response)
async def get_sitemap(game_service: GameService = Depends(get_game_service),
                      user_service: UserService = Depends(get_user_service)):
    games = await game_service.get_catalog(limit=5000)
    users = await user_service.get_all_users()

    static_pages = [
        f"{settings.SITE_DOMAIN}/",
        f"{settings.SITE_DOMAIN}/games",
    ]

    xml_items = []

    for url in static_pages:
        xml_items.append(f"<url><loc>{url}</loc><priority>1.0</priority></url>")

    for game in games:
        game_url = f"{settings.SITE_DOMAIN}/games/{game.uuid}"
        xml_items.append(f"<url><loc>{game_url}</loc><priority>0.8</priority></url>")

    for user in users:
        user_url = f"{settings.SITE_DOMAIN}/users/{user.uuid}"
        xml_items.append(f"<url><loc>{user_url}</loc><priority>0.5</priority></url>")

    xml_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  {chr(10).join(xml_items)}\n"
        '</urlset>'
    )

    return Response(content=xml_content, media_type="application/xml")
