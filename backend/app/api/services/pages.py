from typing import List

from ...core.database import view_collection


async def get_discting_page_views() -> List[str]:
    """
    Fetch all page views.
    """
    return await view_collection.distinct("pageID")
