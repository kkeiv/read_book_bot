from aiogram import Dispatcher, types
from lexicon.lexicon import get_text

# create main menu
async def set_main_menu (dp : Dispatcher) -> None:
    main_menu_commands = [
        types.BotCommand(command='/begining', description=get_text('menu_begining')),
        types.BotCommand(command='/continue', description=get_text('menu_continue')),
        types.BotCommand(command='/bookmarks', description=get_text('menu_bookmarks')),
        types.BotCommand(command='/help', description=get_text('menu_help'))
    ]
    await dp.bot.set_my_commands(main_menu_commands)
