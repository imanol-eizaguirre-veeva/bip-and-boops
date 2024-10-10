import logging

from fastapi import APIRouter, status

router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get("/", status_code=status.HTTP_200_OK)
async def default_route():
    """
    Welcome page.
    """
    return {"msg": "Hello World"}
