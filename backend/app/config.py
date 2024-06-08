import os
from pydantic_settings import BaseSettings # BasedSettings moved from pydantic to pydantic_settings

class Settings(BaseSettings):
    """Settings for the application.

    Args:
        BaseSettings (_type_): Pydantic BaseSettings
    """
    data_file: str = 'data.csv'
    log_file: str = 'scraper.log'

    class Config:
        """Configuration for the settings."""
        env_file = ".env"

settings = Settings()
