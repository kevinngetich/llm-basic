from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "LLM Backend API"
    deepseek_base_url: str
    deepseek_api_key: str
    deepseek_model: str
    openrouter_base_url: str
    openrouter_api_key: str
    openrouter_model: str

    class Config:
        env_file = ".env"

settings = Settings()