from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Database:
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_url: str


@dataclass
class Config:
    tg_bot: TgBot
    database: Database


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"), admin_ids=list(map(int, env.list("ADMIN_IDS")))
        ),
        database=Database(
            db_name=env("DB_NAME"),
            db_user=env("DB_USER"),
            db_port=env("DB_PORT"),
            db_password=env("DB_PASS"),
            db_host=env("DB_HOST"),
            db_url=f"postgresql+asyncpg://{env.str('DB_USER')}:{env.str('DB_PASS')}@{env.str('DB_HOST')}:{env.str('DB_PORT')}/{env.str('DB_NAME')}",
        ),
    )
