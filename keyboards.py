from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from settings import ME_LINK


def create_keyboard(func):
    def wrapper() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        func(keyboard)
        return keyboard.as_markup()

    return wrapper


@create_keyboard
def start_keyboard(keyboard: InlineKeyboardBuilder):
    keyboard.add(InlineKeyboardButton(text="🔥 SI 🔥", callback_data="next"))


@create_keyboard
def escribeme_button(keyboard: InlineKeyboardBuilder):
    keyboard.add(InlineKeyboardButton(text="🤑 Escribeme 🤑", url=ME_LINK))


@create_keyboard
def incio_keyboard(keyboard: InlineKeyboardBuilder):
    keyboard.add(InlineKeyboardButton(text="💸 INICIO 💸", url=ME_LINK))


def next_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text="🚀START🚀")]])
    return keyboard


@create_keyboard
def send_first_video(keyboard: InlineKeyboardBuilder):
    keyboard.add(InlineKeyboardButton(text="🙏 CAMBIA TU VIDA AHORA 🙏", url=ME_LINK))


@create_keyboard
def ganar_keyboard(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="🇲🇽 GANAR DINERO 🇲🇽", url=ME_LINK))
