import os
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo

from pathlib import Path
from dotenv import load_dotenv, find_dotenv


def validate_api_key_value(value: Optional[str], field_name: str) -> Optional[str]:
    """Reject malformed or placeholder provider values before they reach runtime code."""
    if value is None:
        return None

    cleaned = str(value).strip().strip('"').strip("'")
    if not cleaned:
        return None

    placeholder_values = {
        "your_api_key_here",
        "changeme",
        "replace_me",
        "demo",
        "example",
        "test",
        "placeholder",
    }

    lowered = cleaned.lower()
    if lowered in placeholder_values:
        return None

    if cleaned.startswith(("http://", "https://")):
        return None

    if field_name == "OPEN_METEO_API_KEY" and ("open-meteo" in lowered or "api.open-meteo" in lowered):
        return None

    return cleaned


# Ensure .env from project root is loaded into environment variables
env_file_path = find_dotenv(usecwd=True)
if not env_file_path:
    env_file_path = str(Path(__file__).resolve().parent.parent.parent / ".env")
load_dotenv(env_file_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "AgriGen AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # Database settings
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "agrigen_db"
    DATABASE_URL: Optional[str] = None

    # LLM & Weather API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    OPEN_METEO_API_KEY: Optional[str] = os.getenv("OPEN_METEO_API_KEY")
    LLM_MODEL: str = "gpt-4o-mini"

    @field_validator("OPENAI_API_KEY", "GEMINI_API_KEY", "GROQ_API_KEY", "OPEN_METEO_API_KEY", mode="before")
    @classmethod
    def clean_api_keys(cls, value: Optional[str], info: ValidationInfo) -> Optional[str]:
        field_name = info.field_name
        return validate_api_key_value(value, field_name)

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> str:
        if isinstance(v, str):
            return v
        return "sqlite:///./agrigen.db"

    # CORS Origins
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    model_config = SettingsConfigDict(env_file=env_file_path if os.path.exists(env_file_path) else ".env", case_sensitive=True, extra="ignore")


settings = Settings()
