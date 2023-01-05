from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import get_text

# @brief create keyboard for paginated text
def create_pagination_keyboard (*buttons: str) -> InlineKeyboardMarkup:
    # create instance of keyboard
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()

    # add buttons into keyboard
    pagination_kb.row(*[InlineKeyboardButton(get_text(button), callback_data=button) for button in buttons])

    return pagination_kb