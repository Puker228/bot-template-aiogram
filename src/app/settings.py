from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    BOT_TOKEN: str
    ADMIN_IDS: List[str]

    @property
    def get_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_bot_id(self):
        return self.BOT_TOKEN

    def get_user_ids(self):
        return self.ADMIN_IDS

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()