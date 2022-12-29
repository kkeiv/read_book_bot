from dataclasses import dataclass
from environs import Env

# class of bot`s secrets
@dataclass
class TgBot:
    token: str          # token of bot
    admin: list[int]    # list of admin IDs

# class of config
@dataclass
class Config:
    tg_bot : TgBot      # bot`s class

def load_config (path: str | None) -> Config:
    env: Env = Env()                # Create exemplar of Env
    env.read_env(path)              # read file .env and load into OS environment

    return Config(tg_bot=TgBot(token=env('BOT_IDEAL_FIGURE_ASSISTANT_TOKEN'),     # Сохраняем значение переменной окружения в переменную bot_token
                    admin=list(map(int, env.list('BOT_IDEAL_FIGURE_ASSISTANT_ADMIN_ID')))))     # Преобразуем значение переменной окружения к типу int

