from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str              # telegram access token
    admin_ids: list[int]    # list of admin`s ids

@dataclass
class Config:
    tg_bot: TgBot           # main bot configuration

# @brief: load configuration into main structure "Config"
def load_config (path : str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('READ_BOOK_BOT_TOKEN'),
                                admin_ids=list(map(int, env.list('READ_BOOK_BOT_ADMIN')))))




