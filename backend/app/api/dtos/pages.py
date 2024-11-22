from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, UUID4, field_validator


class PageBase(BaseModel):
    """
    Base model for the Page entity.

    This model is used as the base with all shared information, which is the
    information that will be passed in the responses.
    """

    # We define this value as a string because this is how we are storing it
    # in the database, and how it is displayed after serialization.
    # There is a custom validator to verify that it can be transformed to a
    # valid UUID4 object.
    page_id: str = Field(alias="pageID")

    @field_validator("page_id")
    def is_valid_uuid4(cls, value: str):
        try:
            UUID(value, version=4)
        except ValueError:
            raise ValueError(f"{value} is not a valid UUID4")
        return value
