from copy import deepcopy

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from database.database import users_db, user_dict_template
from services.file_handling import book

from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.bookmarks_kb import create_bookmark_kb, create_edit_kb
from lexicon.lexicon import get_text

# @brief handler for "start" command '/start'
async def process_command_start (message : Message) -> None:
    # answer with wellcome text
    answer : str = get_text(message.text)
    await message.answer(answer)

    #save new user into db
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy (user_dict_template)

# @brief handler for "help" command '/help'
async def process_command_help (message : Message) -> None:
    # answer with help text
    answer : str = get_text(message.text)
    await message.answer(answer)

# @brief handler for "start from begining" command '/begining'
async def process_command_beginning (message : Message) -> None:
    # move position to first page
    users_db[message.from_user.id]['page'] = 1
    # get text of first page
    text = book[users_db[message.from_user.id]['page']]

    # prepare answer with new inline markup
    await message.answer(text = text,
                        reply_markup = create_pagination_keyboard(
                            "backward",
                            f"{users_db[message.from_user.id]['page']}/{len(book)}",
                            "forward"
                        )
                )

# @brief handler for "continue reading" command '/continue'
async def process_command_continue (message : Message) -> None:
    # get text of first page
    text = book[users_db[message.from_user.id]['page']]

    # prepare answer with new inline markup
    await message.answer(text = text,
                        reply_markup = create_pagination_keyboard(
                            "backward",
                            f"{users_db[message.from_user.id]['page']}/{len(book)}",
                            "forward"
                        )
    )

# @brief handler for "edit bookmarks" command '/bookmarks'
async def process_command_bookmarks (message : Message) -> None:
    # form replay based on bookmarks of user
    if users_db[message.from_user.id]['bookmarks']:         # user have bookmarks
        await message.answer(text = get_text(message.text),
                    reply_markup = create_bookmark_kb(*users_db[message.from_user.id]['bookmarks']))
    else:                                                   # user have no bookmarks
        await message.answer(text = get_text('no_bookmarks'))

# @brief handler for press button "next page"
async def process_press_next (callback : CallbackQuery) -> None:
    # if we must have next page
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        text = book[users_db[callback.from_user.id]['page']]

        # prepare answer with new inline markup
        await callback.message.edit_text(text = text,
                            reply_markup = create_pagination_keyboard(
                                "backward",
                                f"{users_db[callback.from_user.id]['page']}/{len(book)}",
                                "forward"
                            )
        )
    # no next page - just confirm receiving
    await callback.answer()

# @brief handler for press button "previous page"
async def process_press_prev (callback : CallbackQuery) -> None:
    # if we must have next page
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = book[users_db[callback.from_user.id]['page']]

        # prepare answer with new inline markup
        await callback.message.edit_text(text = text,
                            reply_markup = create_pagination_keyboard(
                                "backward",
                                f"{users_db[callback.from_user.id]['page']}/{len(book)}",
                                "forward"
                            )
        )
    # no next page - just confirm receiving
    await callback.answer()

# @brief handler for press button with page number
async def process_press_page (callback : CallbackQuery) -> None:
    # add new bookmark into set of bookmarks for this user
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page'])
    await callback.answer(get_text('bookmark_added'))

# @brief handler for press button with bookmark number
async def process_press_bookmark (callback : CallbackQuery) -> None:
    # move pointer of page number into new position
    users_db[callback.from_user.id]['page'] = int(callback.data)
    # get text for requested page
    text = book[users_db[callback.from_user.id]['page']]

    # edit current message
    await callback.message.edit_text(text = text,
                        reply_markup = create_pagination_keyboard(
                            'backward',
                            f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                            'forward'
                        )
    )
    # mark answer for telegram
    await callback.answer

# @brief handler for press button with "edit bookmark"
async def process_press_editbm (callback : CallbackQuery) -> None:
    # edit current message
    await callback.message.edit_text(text = get_text(callback.data),
                        reply_markup = create_pagination_keyboard(
                            'backward',
                            f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                            'forward'
                        )
    )
    # mark answer for telegram
    await callback.answer

# @brief handler for press button for cancellation of edit bookmark
async def process_press_cancelbm (callback : CallbackQuery) -> None:
    await callback.message.edit_text(text = get_text('cancel_text'))

    # mark answer for telegram
    await callback.answer

# @brief handler for press button with "delete bookmark"
async def process_press_deletebm (callback : CallbackQuery) -> None:
    # remove bokkmark from list
    users_db[callback.from_user.id]['bookmarks'].remove(int(callback.data[:-3]))

    # prepare replay base on amount of bookmarks
    if users_db[callback.from_user.id]['bookmarks']:         # user have bookmarks
        await callback.message.edit_text(text = get_text('/bookmarks'),
                    reply_markup = create_bookmark_kb(*users_db[callback.from_user.id]['bookmarks']))
    else:                                                   # user have no bookmarks
        await callback.answer(text = get_text('no_bookmarks'))

    # mark answer for telegram
    await callback.answer

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



