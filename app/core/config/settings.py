from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SERVER_", extra="ignore")

    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, ge=1, le=65535, description="Server port")

    workers: int = Field(default=1, ge=1, description="Number of worker processes")
    reload: bool = Field(default=False, description="Auto-reload on code changes")


class OpenAPISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OPENAI_", extra="ignore")

    api_key: str = Field(default="api_key")
    base_url: str = Field(default="http://localhost:8080")
    model: str = Field(default="model")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        validate_assignment=True,
    )
    server: ServerSettings = Field(default_factory=ServerSettings)
    openapi: OpenAPISettings = Field(default_factory=OpenAPISettings)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
