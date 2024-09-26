import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from .api.main import api_router
from .core.config import settings


logger = logging.getLogger("uvicorn.error")


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# ["*"] won't work when allow_credentials=True
origins = [
    # localhosts (to access from the browser)
    "http://localhost:4200",
    # 0.0.0.0 (address used inside the frontend code, also from the browser)
    "http://0.0.0.0:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
