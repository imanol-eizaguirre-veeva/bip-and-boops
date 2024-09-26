from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import Field
from pydantic.functional_validators import BeforeValidator
from pydantic_extra_types.country import CountryShortName

from .pages import PageBase


# Represents an ObjectId field in the database.
# It will be represented as `str` on the model so it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class ViewCreate(PageBase):
    """
    Base model for the View entity.

    This model is used as the base with all shared information, which is the
    information that will be passed in the responses.
    """

    country: CountryShortName  # ISO 3166
    browser: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "page_id": "f6943675-1f29-4eef-b0f0-4e47c252a6e7",
                    "country": "Germany",
                    "browser": "Firefox",
                }
            ]
        }
    }


class ViewPublic(ViewCreate):
    """
    Base model for the View entity.

    This model is used as the base with all shared information, which is the
    information that will be passed in the responses.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    utc_date_time: datetime = Field(alias="UTCDateTime")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "_id": "98bcd14f-da02-4fd8-a596-a4f8996001b6",
                    "utc_date_time": "2024-09-20T13:31:37.615+00:00",
                    "page_id": "f6943675-1f29-4eef-b0f0-4e47c252a6e7",
                    "country": "Germany",
                    "browser": "Firefox",
                }
            ]
        }
    }


class ViewPrivate(ViewPublic):
    """
    Complete View model representing every field in the database.
    """

    user_id: str = Field(alias="userID")
    version: Optional[int] = Field(alias="__v", default=0)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "_id": "98bcd14f-da02-4fd8-a596-a4f8996001b6",
                    "utc_date_time": "2024-09-20T13:31:37.615+00:00",
                    "page_id": "f6943675-1f29-4eef-b0f0-4e47c252a6e7",
                    "country": "Germany",
                    "browser": "Firefox",
                    "user_id": "3",
                    "__v": 0,
                }
            ]
        }
    }
