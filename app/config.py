import os
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://postgres:aaliyah@localhost:5432/bookitdb"
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    environment: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()