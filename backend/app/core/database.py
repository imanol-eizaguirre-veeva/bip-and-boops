import pytz
import motor.motor_asyncio

from bson.codec_options import CodecOptions

from .config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL,
    uuidRepresentation="standard",
)

database = client.analytics
view_collection = database.get_collection("pageviews")

# PyMongo hacky way of dealing with TZ aware datetime objects
# In this project is used exclusively for fetch operations
tz_aware_views_collection = view_collection.with_options(
    codec_options=CodecOptions(
        tz_aware=True,
        tzinfo=pytz.timezone(settings.TIMEZONE),
    )
)
