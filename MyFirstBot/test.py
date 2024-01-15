import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

#2

TOKEN = os.getenv('TOKEN')
# TOKEN = '6921460187:AAFExP_ipqdXQOkRoonudIZg6CbkAnOev9w'
bot=Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

#3
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Этот бот предназначен для транслитерации имени согласно приказу МИД РФ от 2020 года с русского языка на латиницу.\nВвeдите ваше полное имя:'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


#4
def translitaration(name):
    from string import ascii_letters
    alphabet = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
                'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
                'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
                'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
                'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
                'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y',
                'Ъ': 'IE', 'Ь':'', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}

    name = name.strip()
    result = ''
    for i in name:
        if i in ascii_letters:
            result += i
        elif i.isupper():
            result += alphabet[i]
        elif i.islower():
            result += alphabet[i.upper()].lower()
        else:
            result += i
    return result.title()


@dp.message()
async def send_(message: Message):
    text = translitaration(message.text)
    logging.info(f'{message.from_user.first_name} {message.from_user.id} написал {message.text}')
    await message.answer(text=text)

#5
if __name__ == '__main__':
    dp.run_polling(bot)
