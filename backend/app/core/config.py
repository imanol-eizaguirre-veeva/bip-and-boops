from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Read environment variables from .env file
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    # Define all environment variables
    PROJECT_NAME: str = "Bip and Boops"
    ANALYTICS_PAGE_ACTIVE_USERS_TIME_PERIOD: int = 1800000
    API_V1_STR: str = "/api/v1"
    TIMEZONE: str = "Europe/Berlin"

    # Sensitive values that will be read from an .env file, in case it is provided
    MONGODB_URL: str = "change_me"


settings = Settings()
