import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

#2

TOKEN = '6856434115:AAH4-Umo0hEr9fDcxg9rpZMF3p74f9PpdE4'
bot=Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


#3
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


#4


@dp.message()
async def send_(message: Message):
    text = translitaration(message.text)
    logging.info(f'{message.from_user.first_name} {message.from_user.id} написал {message.text}')
    await message.answer(text=text)

#5
if __name__ == '__main__':
    dp.run_polling(bot)
