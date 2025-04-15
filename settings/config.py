from builtins import bool, int, str
from pathlib import Path
from pydantic import Field, AnyUrl, DirectoryPath
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Server configuration
    server_base_url: AnyUrl = Field(default='http://localhost', description="Base URL of the server")
    server_download_folder: str = Field(default='downloads', description="Folder for storing downloaded files")

    # Security and authentication configuration
    secret_key: str = Field(default="secret-key", description="Secret key for encryption")
    algorithm: str = Field(default="HS256", description="Algorithm used for encryption")
    access_token_expire_minutes: int = Field(default=30, description="Expiration time for access tokens in minutes")
    admin_user: str = Field(default='admin', description="Default admin username")
    admin_password: str = Field(default='secret', description="Default admin password")
    debug: bool = Field(default=False, description="Debug mode outputs errors and sqlalchemy queries")
    jwt_secret_key: str = "a_very_secret_key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15  # 15 minutes for access token
    refresh_token_expire_minutes: int = 1440  # 24 hours for refresh token

    # Database configuration
    database_url: str = Field(default='postgresql+asyncpg://user:password@postgres/myappdb', description="URL for connecting to the database")
    postgres_user: str = Field(default='user', description="PostgreSQL username")
    postgres_password: str = Field(default='password', description="PostgreSQL password")
    postgres_server: str = Field(default='localhost', description="PostgreSQL server address")
    postgres_port: str = Field(default='5432', description="PostgreSQL port")
    postgres_db: str = Field(default='myappdb', description="PostgreSQL database name")

    # Discord configuration
    discord_bot_token: str = Field(default='NONE', description="Discord bot token")
    discord_channel_id: int = Field(default=1234567890, description="Default Discord channel ID for the bot to interact", example=1234567890)

    # OpenAI Key 
    openai_api_key: str = Field(default='NONE', description="Open AI API Key")
    max_login_attempts: int = Field(default=5, description="Max login attempts", example=5)
    send_real_mail: bool = Field(default=False, description="Whether to send real emails or use a mock service")

    # SMTP (email) configuration
    smtp_host: str = Field(default='sandbox.smtp.mailtrap.io', description="SMTP server hostname")
    smtp_port: int = Field(default=587, description="SMTP server port")
    smtp_username: str = Field(default='559910da9bdbc6', description="SMTP username (email account)")
    smtp_password: str = Field(default='f857d1faae6303', description="SMTP password")
    smtp_sender_email: str = Field(default='test@myapp.com', description="Default sender email address")

    class Config:
        env_file = ".env"  # Path to the .env file
        env_file_encoding = 'utf-8'

# Instantiate settings to be imported in your application
settings = Settings()
