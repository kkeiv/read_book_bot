from aiogram import Dispatcher
from aiogram.types import Message
from lexicon.lexicon import get_text

# @brief answer for all anknown messages
async def send_echo(message : Message) -> None:
    text_beg = get_text('unknown_message')
    await message.answer(f'{text_beg} {message.text}')   # just echo response

# @brief register all alternative handlers
def register_other_handlers (dp: Dispatcher) -> None:
    dp.register_message_handler(send_echo)              # all anknown messages