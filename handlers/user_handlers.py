from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

# @brief handler for "start" command
async def process_command_start (message : Message) -> None:
    pass

# @brief handler for "help" command
async def process_command_help (message : Message) -> None:
    pass

# @brief handler for "start from begining" command
async def process_command_beginning (message : Message) -> None:
    pass

# @brief handler for "continue reading" command
async def process_command_continue (message : Message) -> None:
    pass

# @brief handler for "edit bookmarks" command
async def process_command_bookmarks (message : Message) -> None:
    pass

# @brief handler for press button "next page"
async def process_press_next (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button "previous page"
async def process_press_prev (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button with page number
async def process_press_page (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button with bookmark number
async def process_press_bookmark (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button with "edit bookmark"
async def process_press_editbm (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button for cancellation of edit bookmark
async def process_press_cancelbm (callback : CallbackQuery) -> None:
    pass

# @brief handler for press button with "delete bookmark"
async def process_press_deletebm (callback : CallbackQuery) -> None:
    pass

# @brief register all user`s handlers
def register_user_handlers (dp : Dispatcher) -> None:
    dp.register_message_handler(process_command_start, commands=['start'])
    dp.register_message_handler(process_command_help, commands=['help'])
    dp.register_message_handler(process_command_beginning, commands=['begining'])
    dp.register_message_handler(process_command_continue, commands=['continue'])
    dp.register_message_handler(process_command_bookmarks, commands=['bookmarks'])

    dp.register_callback_query_handler(process_press_next, text="forward")
    dp.register_callback_query_handler(process_press_prev, text="backward")
    dp.register_callback_query_handler(process_press_page,
                        lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
    dp.register_callback_query_handler(process_press_bookmark,
                        lambda x: x.isdigit())
    dp.register_callback_query_handler(process_press_editbm, text="edit_bookmarks")
    dp.register_callback_query_handler(process_press_cancelbm, text="cancel")
    dp.register_callback_query_handler(process_press_deletebm,
                        lambda x: 'del' in x.data and x.data[:-3].isdigit())



