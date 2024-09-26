import logging

from datetime import datetime
from pydantic_extra_types.country import CountryShortName
from typing import Any, List, Optional
from zoneinfo import ZoneInfo

from ...core.config import settings
from ...core.database import view_collection
from ..dtos.pages import PageBase
from ..dtos.views import (
    ViewCreate,
    ViewPrivate,
)

logger = logging.getLogger("uvicorn.error")


async def get_views(
    countries: Optional[List[CountryShortName]] = None,
    browsers: Optional[List[str]] = None,
    page_id: Optional[str] = None,
) -> list:
    """
    Returns every page matching the provided criteria.
    """
    query_filters = {}
    if countries:
        query_filters.update({"country": {"$in": countries}})
    if browsers:
        query_filters.update({"browser": {"$in": browsers}})
    if page_id:
        query_filters.update(
            PageBase(
                pageID=page_id,
            ).model_dump(
                by_alias=True,
                mode="json",
            )
        )

    return await view_collection.find(query_filters).to_list()


async def add_new_view(
    data: ViewPrivate,
    user_id: str,
):
    """
    Create a new view.
    """
    validated_data = ViewPrivate(
        userID=user_id,
        UTCDateTime=datetime.now(ZoneInfo(settings.TIMEZONE)),
        **data.model_dump(by_alias=True),
    )
    new_view = await view_collection.insert_one(
        validated_data.model_dump(by_alias=True, exclude=["id"], mode="json")
    )
    return await view_collection.find_one({"_id": new_view.inserted_id})
