import logging
from typing import Any, Annotated, List

from fastapi import APIRouter, Depends, status

from ..dtos.auth import User

from ..services.auth import get_current_active_user
from ..services.pages import get_discting_page_views

router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get(
    "/",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
)
async def get_pages_list(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """
    Retrieve the list of distinct page IDs.
    """
    return await get_discting_page_views()
