from builtins import bool, int, str
from pathlib import Path 
from typing import Optional
from pydantic import  Field, AnyUrl, AliasChoices
#DirectoryPath,
from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    # Pydantic v2 settings config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid",        # keep strict: unknown keys raise an error
        case_sensitive=False,  # allow JWT_SECRET or jwt_secret, etc.
    )

    # -------------------------
    # General / server config
    # -------------------------
    max_login_attempts: int = Field(
        default=3, description="Background color of QR codes"  # (leaving as-is from your file)
    )
    server_base_url: AnyUrl = Field(
        default="http://localhost", description="Base URL of the server"
    )
    server_download_folder: str = Field(
        default="downloads", description="Folder for storing downloaded files"
    )

    # -------------------------
    # Security / encryption
    # -------------------------
    secret_key: str = Field(default="secret-key", description="Secret key for encryption")
    algorithm: str = Field(default="HS256", description="Algorithm used for encryption")

    # -------------------------
    # Admin / debug
    # -------------------------
    admin_user: str = Field(default="admin", description="Default admin username")
    admin_password: str = Field(default="secret", description="Default admin password")
    debug: bool = Field(
        default=False, description="Debug mode outputs errors and SQLAlchemy queries"
    )

    # -------------------------
    # JWT / tokens
    # -------------------------
    # Accept jwt_secret / JWT_SECRET / jwt_secret_key from .env, but expose as jwt_secret_key in code
    jwt_secret_key: str = Field(
        default="a_very_secret_key",
        validation_alias=AliasChoices("jwt_secret", "JWT_SECRET", "jwt_secret_key"),
        description="JWT signing secret",
    )
    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = Field(
        default=30, description="Expiration time for access tokens in minutes"
    )
    refresh_token_expire_minutes: int = Field(
        default=1440, description="24 hours for refresh token"
    )

    # -------------------------
    # Database configuration
    # -------------------------
    database_url: str = Field(
        default="postgresql+asyncpg://user:password@postgres/myappdb",
        description="URL for connecting to the database",
    )

    # Optional components to build a URL (if you ever switch away from database_url)
    postgres_user: str = Field(default="user", description="PostgreSQL username")
    postgres_password: str = Field(default="password", description="PostgreSQL password")
    postgres_server: str = Field(default="localhost", description="PostgreSQL server")
    postgres_port: int = Field(default=5432, description="PostgreSQL port")
    postgres_db: str = Field(default="myappdb", description="PostgreSQL database name")

    # -------------------------
    # Discord configuration
    # -------------------------
    discord_bot_token: str = Field(default="NONE", description="Discord bot token")
    discord_channel_id: int = Field(
        default=1234567890,
        description="Default Discord channel ID for the bot to interact",
    )

    # -------------------------
    # OpenAI / 3rd-party
    # -------------------------
    openai_api_key: str = Field(default="NONE", description="OpenAI API key")

    # -------------------------
    # Email settings
    # -------------------------
    send_real_mail: bool = Field(default=False, description="use mock")
    smtp_server: str = Field(default="smtp.mailtrap.io", description="SMTP server")
    smtp_port: int = Field(default=2525, description="SMTP port")
    smtp_username: str = Field(
        default="your-mailtrap-username", description="SMTP username"
    )
    smtp_password: str = Field(
        default="your-mailtrap-password", description="SMTP password"
    )

    # Helper to prefer database_url, else build from pieces (if you ever need it)
    @property
    def sqlalchemy_database_uri(self) -> str:
        if self.database_url:
            return self.database_url
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
        )


# Instantiate and (optionally) provide a getter for DI
settings = Settings()

def get_settings() -> Settings:
    return settings

