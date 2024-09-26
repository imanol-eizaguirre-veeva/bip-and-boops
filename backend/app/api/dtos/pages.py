from typing import Any
from uuid import UUID, uuid4

from pydantic import (
    BaseModel,
    Field,
    UUID4,
)


class PageBase(BaseModel):
    """
    Base model for the Page entity.

    This model is used as the base with all shared information, which is the
    information that will be passed in the responses.
    """

    page_id: UUID = Field(alias="pageID", default_factory=uuid4)
