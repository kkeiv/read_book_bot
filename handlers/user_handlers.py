from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove
#import datetime
#import time
from utils.ulils import is_new_user, is_admin, is_private, is_registred
from models.models import create_user, users
from models.methods import save_users_file

from keyboards.keyboard_utils import keybord_start, keybord_register

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    id = message.from_user.id
    # новый пользователь
    if is_new_user(id):
        new_user = create_user(firstName=message.from_user.first_name,
                lastName=message.from_user.last_name,
                nickName=message.from_user.username,
                isBot=message.from_user.is_bot,
                tgLang=message.from_user.language_code)
        users[id] = new_user
        save_users_file(users)
        await message.answer(f'Привет {new_user.udata.fname} {new_user.udata.fname}!\nЯ вижу ты здесь первый раз. Давай начнем со знакомства.\n\nЖми "Заполнить анкету"', reply_markup=keybord_start)
        return
    else:
        if is_admin(id):
            await message.answer(f'Привет admin {users[id].udata.fname} {users[id].udata.fname}!\n\nХотите узнать что было в период вашего отсутствия?')
        elif is_private(id):
            await message.answer(f'Привет {users[id].udata.fname} {users[id].udata.fname}!\n\nРады вас видеть снова.\nХотите посмотреть состояние ваших подписок?')
        elif is_registred(id):
            await message.answer(f'Привет {users[id].udata.fname} {users[id].udata.fname}!\n\nУ нас есть кое что интересное для вас')
        else:
            await message.answer(f'Привет {users[id].udata.fname} {users[id].udata.fname}!\n\nРады вас видеть.\nПредлагаю пройти короткую регистрацию. Это позволит нам более эффективно взаимодействовать в будущем.\n\nПосле регистрации вам станет доступно больше информации', reply_markup=keybord_register)
        return
    await message.answer(f'Не знаю как мы сюда попали, но давайте попробуем выбраться вместе 0x001')
#    await message.answer(f'А мы с вами не знакомы', reply_markup=keybord_start)


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(f'Давайте я вам помогу\n\nКакую информацию вы ищите?')


# Этот хэндлер будет срабатывать на остальные текстовые сообщения
async def process_other_text_answers(message: Message):
    print(message.text)
    txt = f'Мы с вами еще не знакомы\n\nМожно узнать вас поближе. Это поможет мне более точно предоставлять вам информацию'
    await message.answer(txt)



# реакция на кнопки

# Этот хэндлер будет срабатывать на остальные текстовые сообщения
async def process_fill_anket_start(message: Message):
    await message.answer(f'Отлично!\nЭто не займет много времени', reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на остальные текстовые сообщения
async def process_anonium_user(message: Message):
    txt = f'Хорошо.\nВы всегда можете зарегистрироваться позже, нажава кнопку "Заполнить анкету"\n\nВот тут 👇👇👇'
    await message.answer(txt, reply_markup=keybord_register)
    await message.answer("👇")
