import os

class Settings:
    SECRET_KEY = "supersecret"
    DATABASE_URL = "postgresql://user:pass@db:5432/app"
    REDIS_URL = "redis://redis:6379"

settings = Settings()
