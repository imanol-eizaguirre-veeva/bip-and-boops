import logging

from datetime import datetime, timezone
from pydantic_extra_types.country import CountryShortName
from typing import List, Optional

from ...core.database import tz_aware_views_collection, view_collection
from ..dtos.pages import PageBase
from ..dtos.views import ViewPublic

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
    # for the return value, use the tz aware `find_one`
    return await tz_aware_views_collection.find(query_filters).to_list()


async def add_new_view(data: ViewPublic):
    """
    Create a new view.
    """

    validated_data = ViewPublic(
        UTCDateTime=datetime.now(timezone.utc),
        **data.model_dump(by_alias=True),
    )
    # TODO: insert UUID as str
    new_view = await view_collection.insert_one(
        validated_data.model_dump(by_alias=True, exclude=["id"])
    )
    # for the return value, use the tz aware `find_one`
    return await tz_aware_views_collection.find_one(
        {"_id": new_view.inserted_id}
    )
