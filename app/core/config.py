from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME:str = "Voice Assistant API"
    DEBUG:bool = True

    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS:List[str]=[
        "http://localhost:3000/",
        "http://localhost:8000/", # FIXME
    ]

    DATABASE_URL:str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "voice_assistant"

    OPENAI_API_KEY: str = ""
    AI_MODEL:str = "gpt-3.5-turbo"

    class Config:
        env_file = ".env"

settings = Settings()
