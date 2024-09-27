import logging

from datetime import datetime, timedelta
from typing import Any, Annotated
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, Path, status

from ...core.config import settings
from ..dtos.auth import User
from ..dtos.stats import StatsBase
from ..services.auth import get_current_active_user
from ..services.stats import get_user_count_in_period


router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.get(
    "/page/{page_id}/active",
    response_model=StatsBase,
    status_code=status.HTTP_200_OK,
)
async def get_stats_for_page_last_30_min(
    current_user: Annotated[User, Depends(get_current_active_user)],
    page_id: Annotated[str, Path(title="The UUID of the page to get")],
) -> Any:
    """
    Returns the number of unique users having been active on
    the page in a given time period
    """
    period_duration = settings.ANALYTICS_PAGE_UNIQUE_VISITORS_TIME_PERIOD
    start_date = datetime.now(ZoneInfo(settings.TIMEZONE)) - timedelta(
        milliseconds=period_duration
    )
    # it's not implementing a 404 in case the page does not exist, but
    # the Frontend is handling it as 404
    value = await get_user_count_in_period(page_id, start_date)

    return StatsBase(period_duration=period_duration, value=value)
