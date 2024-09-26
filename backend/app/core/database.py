import motor.motor_asyncio

from .config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL,
    uuidRepresentation="standard",
)

database = client.analytics
view_collection = database.get_collection("pageviews")


# Mock Outh2
fake_users_db = {
    "1234567890": {
        # this attribute is not used to find the user, the key of the dict is
        "username": "1234567890",
        "full_name": "John Doe",
        "email": "johndoe@veeva.com",
        # dehasehd password: secret
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}
