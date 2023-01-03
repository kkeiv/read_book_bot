import asyncio
import logging

from aiogram import Dispatcher, Bot

from config_data.config import Config, load_config

from services.file_handling import book, prepare_book, BOOK_PATH
from keyboards.main_menu import set_main_menu
from handlers.other_handlers import register_other_handlers
from handlers.user_handlers import register_user_handlers

# initialize logger
logger = logging.getLogger(__name__)

# @brief register handlers from all modules
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)

# @brief main starting
async def main():

    # create and load configurations
    config: Config = load_config()

    prepare_book(BOOK_PATH)

    # create and initialize bot
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    # create and initialize dispatcher
    dp: Dispatcher = Dispatcher(bot=bot)

    # prepare main menu
    await set_main_menu(dp)

    # start pooling
    try:
        await dp.start_polling()
    finally:
        await bot.close()


# main point of statring
if __name__ == '__main__':
    try:
        # try to start main programm
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # write log event if somone going wrong
        logger.error('Bot Stopped by exeption')
