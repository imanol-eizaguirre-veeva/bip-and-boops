import logging

from datetime import datetime

from ...core.database import view_collection


logger = logging.getLogger("uvicorn.error")


async def get_active_users_count_in_period(
    page_id: str,
    start_date: datetime,
) -> int:
    """
    Returns the number of users having visited a given page in a given period.
    """
    unique_users = await view_collection.distinct(
        "userID",
        {
            "pageID": page_id,
            "UTCDateTime": {"$gte": start_date},
        },
    )
    return len(unique_users)
