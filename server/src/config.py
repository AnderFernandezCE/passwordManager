from typing import Any

from pydantic import MySQLDsn
from pydantic_settings import BaseSettings
from src.constants import Environment

class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = ""

    DATABASE_URL: MySQLDsn

    SITE_DOMAIN: str = "0.0.0.0"
    SITE_PORT:int = 8000

    ENVIRONMENT: Environment = Environment.PRODUCTION

    RESEND_API: str
    #SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"



settings = AppSettings()

app_configs: dict[str, Any] = {"title": "Reposearch API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs