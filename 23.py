import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Токен бота, полученный от @BotFather
TOKEN = '8182847211:AAHLZjbnVwbyMgdFQGJYkQIZNHtN8AWFnoQ'

async def command_start_handler(message: Message):
    await message.answer(f"Привет!")

async def command_google_handler(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть Google",
                    web_app=WebAppInfo(url='https://www.google.com')
                )
            ]
        ]
    )
    await message.answer("Нажмите на кнопку, чтобы открыть Google", reply_markup=markup)

async def main():
    # Создаем объект бота
    bot = Bot(TOKEN)
    
    # Создаем объект Dispatcher и регистрируем обработчики
    dp = Dispatcher(bot)
    dp.message.register(command_start_handler, CommandStart())
    dp.message.register(command_google_handler, Command('google'))

    # Запускаем бота
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
