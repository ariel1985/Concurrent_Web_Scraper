import os
from pydantic_settings import BaseSettings # BasedSettings moved from pydantic to pydantic_settings

class Settings(BaseSettings):
    data_file: str = 'data.csv'
    log_file: str = 'scraper.log'

    class Config:
        env_file = ".env"

settings = Settings()
