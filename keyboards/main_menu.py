from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем объект клавиатуры
keybord_start: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
keybord_register: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

# Создаем объекты кнопок
buttun_register_test: KeyboardButton = KeyboardButton("Заполнить анкету")
buttun_anonim: KeyboardButton = KeyboardButton("Анонимный пользователь")

# Добавляем кнопки в клавиатуру методом add
keybord_start.add(buttun_register_test, buttun_anonim)

keybord_register.add(buttun_register_test)