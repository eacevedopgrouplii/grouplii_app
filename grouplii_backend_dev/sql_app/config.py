from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

env_location = Path("./.env").resolve()

load_dotenv()

class Settings(BaseSettings):
    MAIL_USERNAME: str 
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = env_location
        env_file_encoding = 'utf-8'