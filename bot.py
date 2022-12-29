from config_data.config import load_config
from aiogram import Bot, Dispatcher, executor
import handlers.user_handlers
from models.methods import load_users_file
from models.models import Users, users


config = load_config(None)
print(config)

# Создаем объекты бота и диспетчера
bot: Bot = Bot(config.tg_bot.token)
dp: Dispatcher = Dispatcher(bot)

# подгружаем базу пользователей
users = load_users_file()


dp.register_message_handler(handlers.user_handlers.process_start_command, commands='start')
dp.register_message_handler(handlers.user_handlers.process_help_command, commands='help')

dp.register_message_handler(handlers.user_handlers.process_fill_anket_start, text='Заполнить анкету')
dp.register_message_handler(handlers.user_handlers.process_anonium_user, text='Анонимный пользователь')
#dp.register_message_handler(process_stat_command, commands='stat')
#dp.register_message_handler(process_cancel_command, commands='cancel')
dp.register_message_handler(handlers.user_handlers.process_other_text_answers)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)