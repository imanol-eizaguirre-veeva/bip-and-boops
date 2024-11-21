import logging
from typing import List

from fastapi import APIRouter, status

from ..services.pages import get_distinct_page_views

router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get(
    "/",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
)
async def get_pages_list():
    """
    Retrieve the list of distinct page IDs.
    """
    return await get_distinct_page_views()
