from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import get_text
from services.file_handling import book

# @brief create keyboard for bookmarks selection
def create_bookmark_kb(*args : int) -> InlineKeyboardMarkup:
    # create keyboard instance
    bookmark_kb : InlineKeyboardMarkup = InlineKeyboardMarkup()

    # fill with known bookmarks
    for bnumber in sorted(args):
        bookmark_kb.add(InlineKeyboardButton(text=f'{bnumber} - {book[bnumber][:100]}',
                                             callback_data=str(bnumber)))

    # add two buttons for edit bokkmarks and cancel this sta
    bookmark_kb.add(InlineKeyboardButton(text=get_text('edit_bookmarks'), callback_data='edit_bookmarks'))
    bookmark_kb.add(InlineKeyboardButton(text=get_text('cancel'), callback_data='cancel'))

    return bookmark_kb

# @brief create keyboard for bookmarks edit
def create_edit_kb(*args : int) -> InlineKeyboardMarkup:
    # create keyboard instance
    bookmark_kb : InlineKeyboardMarkup = InlineKeyboardMarkup()

    # fill with known bookmarks
    del_txt : str = get_text('del')
    for bnumber in sorted(args):
        bookmark_kb.add(InlineKeyboardButton(text=f'{del_txt}{bnumber} - {book[bnumber][:100]}',
                                             callback_data=str(bnumber)))

    # add button for cancel of registration
    bookmark_kb.add(InlineKeyboardButton(text=get_text('cancel'), callback_data='cancel'))

    return bookmark_kb

