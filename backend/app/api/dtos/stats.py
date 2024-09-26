from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import (
    BaseModel,
)


class StatsBase(BaseModel):
    """
    Number of milliseconds that have been removed from current date in order
    to retrieve value.
    """

    period_duration: int
    value: int
