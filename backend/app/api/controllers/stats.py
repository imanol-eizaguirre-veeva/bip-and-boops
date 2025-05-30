import logging

from datetime import datetime, timedelta
from typing import Any, Annotated
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Path, status

from ...core.config import settings
from ..dtos.stats import StatsBase
from ..services.stats import get_active_users_count_in_period


router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get(
    "/page/{page_id}/active",
    response_model=StatsBase,
    status_code=status.HTTP_200_OK,
)
async def get_active_users_for_page(
    page_id: Annotated[str, Path(title="The UUID of the page to get")],
) -> Any:
    """
    Returns the number of unique users having been active on
    the page in a period of time defined in the settings.
    """
    period_duration = settings.ANALYTICS_PAGE_ACTIVE_USERS_TIME_PERIOD
    start_date = datetime.now(ZoneInfo(settings.TIMEZONE)) - timedelta(
        milliseconds=period_duration
    )
    value = await get_active_users_count_in_period(page_id, start_date)

    return StatsBase(period_duration=period_duration, value=value)
