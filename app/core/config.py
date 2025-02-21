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
    GEMINI_API_KEY: str = ""
    
    GEMINI_AI_MODEL:str = ""
    OPENAI_AI_MODEL:str = ""

    PROMPT_TEMPLATE:str ="""
        Analyze the following user input and determine the intent. 
        Respond in JSON format with these fields:
        - intent: one word that defines what the intention of the text is
        - confidence: A float between 0 and 1 indicating your confidence in your answer
        - response: A natural language response to the user

        Now analyze this input: "{text}"
        Respond only with the JSON, no other text.
        """
    class Config:
        env_file = ".env"

settings = Settings()
