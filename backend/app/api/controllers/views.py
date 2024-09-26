import logging
from datetime import datetime
from typing import Annotated, Any, List
from zoneinfo import ZoneInfo

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from pydantic_extra_types.country import CountryShortName

from ..dtos.auth import User
from ..dtos.views import (
    ViewCreate,
    ViewPublic,
)
from ..services.auth import get_current_active_user
from ..services.views import (
    add_new_view,
    get_views,
)

router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get(
    "/",
    response_model=List[ViewPublic],
    status_code=status.HTTP_200_OK,
)
async def get_view_list(
    current_user: Annotated[User, Depends(get_current_active_user)],
    countries: Annotated[List[CountryShortName] | None, Query()] = None,
    browsers: Annotated[List[str] | None, Query()] = None,
) -> Any:
    """
    Retrieve all views (that satisfy the filters).
    """
    return await get_views(countries=countries, browsers=browsers)


@router.post(
    "/",
    response_model=ViewPublic,
    status_code=status.HTTP_201_CREATED,
)
async def create_view(
    current_user: Annotated[User, Depends(get_current_active_user)],
    view_in: Annotated[
        ViewCreate,
        Body(
            openapi_examples={
                "existing": {
                    "summary": "Add view to existing page",
                    "description": "Add view to existing page.",
                    "value": {
                        "pageID": "38f92553-00a3-43d1-91fb-9329ce2f3673",
                        "country": "Germany",
                        "browser": "Firefox",
                    },
                },
                "new": {
                    "summary": "Add view to new page.",
                    "description": "Add view to non-existing page.",
                    "value": {
                        "pageID": "98f92553-75a4-12d2-81fb-9329ce2f3673",
                        "country": "Netherlands",
                        "browser": "Chrome",
                    },
                },
            },
        ),
    ],
) -> Any:
    """
    Insert a new view record.

    A unique `id` will be created and provided in the response.
    """
    return await add_new_view(data=view_in, user_id=current_user.username)


@router.get(
    "/page/{page_id}",
    response_model=List[ViewPublic],
    status_code=status.HTTP_200_OK,
)
async def get_view_page_detail(
    current_user: Annotated[User, Depends(get_current_active_user)],
    page_id: Annotated[str, Path(title="The UUID of the page to get")],
) -> Any:
    """
    Retrieve the views of a particular page.
    """
    page_views = await get_views(page_id=page_id)
    if not page_views:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Page ID {page_id} not found",
        )
    return page_views
