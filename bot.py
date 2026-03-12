import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Токен берётся из переменной окружения (для безопасности)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8776133806:AAEaJX9uFjpUtu5NBeLHX0ldHdMIb2sA-X8")

# Ссылка на вашу игру (GitHub Pages)
GAME_URL = "https://narvenolgui.github.io/AgenstvoMozg/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Запустить игру", web_app=WebAppInfo(url=GAME_URL))]
    ])
    await message.answer("Привет! Это профориентационная игра «Агентство Мозг».", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
