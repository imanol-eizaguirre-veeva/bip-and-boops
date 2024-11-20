from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import BaseModel


class StatsBase(BaseModel):
    """
    Generic model for stats.

    @param value: number of returned documents
    @param period_duration: milliseconds since the requested timestamp
    """

    period_duration: int
    value: int
