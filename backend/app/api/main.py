from fastapi import APIRouter

from .controllers import misc, pages, stats, views


api_router = APIRouter()
api_router.include_router(pages.router, prefix="/page", tags=["pages"])
api_router.include_router(stats.router, prefix="/stats", tags=["stats"])
api_router.include_router(views.router, prefix="/view", tags=["views"])
api_router.include_router(misc.router, prefix="", tags=["misc"])
