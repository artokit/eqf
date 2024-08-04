import asyncio
import os
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, ChatJoinRequest
import keyboards
from settings import MEDIA_PATH, ME_LINK
import db_api

router = Router()


@router.chat_join_request()
async def join(update: ChatJoinRequest):
    db_api.add_user(update.from_user.id, update.from_user.username)
    await update.approve()
    await update.bot.send_photo(
        chat_id=update.from_user.id,
        photo=FSInputFile(os.path.join(MEDIA_PATH, "check_bot.png")),
        caption="⛔️PARA!⛔️\n\n"
                "🤖Pasar verificación🤖\n\n"
                "Presione el botón 🚀START🚀",
        reply_markup=keyboards.next_keyboard()
    )


@router.message(Command("start"))
async def start(message: Message):
    db_api.add_user(message.chat.id, message.chat.username)
    await send_start_message(message.bot, message.chat.id)


@router.message(F.text == "🚀START🚀")
async def next_message(message: Message):
    await send_start_message(message.bot, message.chat.id)


async def send_start_message(bot: Bot, chat_id: int):
    await bot.send_photo(
        photo=FSInputFile(os.path.join(MEDIA_PATH, "start.png")),
        chat_id=chat_id,
        caption="Hola 👋🏻\n\n"
                "<b>Estoy aquí para mostrarte una manera fácil de ganar dinero en cualquier lugar! 🤑</b>\n\n"
                "Escríbeme y averigua cómo ganar de 45 mil pesos en 1 hora 👇",
        parse_mode="html",
        reply_markup=keyboards.incio_keyboard()
    )

    await asyncio.sleep(5*60)
    t = "@" + ME_LINK.replace("https://t.me/", "") + "\n"
    await bot.send_photo(
        photo=FSInputFile(os.path.join(MEDIA_PATH, "time_ping.png")),
        chat_id=chat_id,
        reply_markup=keyboards.escribeme_button(),
        caption="Ya ha ganado 9️⃣9️⃣ mil pesos en solo 1 hora con mi ayuda. Hace poco me dieron información privilegiada y aprovechamos esta oportunidad 💵\n\n"
                "Hoy también podrías usar esta información y ganar 😳\n\n"
                "A qué esperas? 🤯\n\n"
                "Solo quedan3️⃣ plazas en el equipo‼️\n\n"
                "Escríbeme y cambiemos tu vida💰👇👇👇\n\n"
                f"{t*3}",
    )
