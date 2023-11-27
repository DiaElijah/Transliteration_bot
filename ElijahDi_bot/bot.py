import logging
import asyncio
import os
from string import punctuation, ascii_lowercase
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# from config import TOKEN

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
dct = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e',
        'ж':'zh', 'з':'z', 'и':'i', 'й':'i', 'к':'k', 'л':'l', 'м':'m',
        'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u',
        'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'shch',
        'ы':'y', 'ь':'ie', 'э':'e', 'ю':'iu', 'я':'ia'}
# r = []

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Я простенький бот, который сделает транслитерацию твоей фамилии, имени и даже отчества в соответствии с Приказом МИД России от 12.02.2020 № 2113.\n \nВведи ФИО кирилицей.'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)
# async def cmd_start(message: types.Message):
#     await message.answer('Привет! Я простенький бот, который сделает транслитерацию твоей фамилии.')

@dp.message()
async def send_echo(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = message.text
    if len([ch for w in text.lower().split() for ch in w if ch in ascii_lowercase]) != 0:
        await bot.send_message(user_id, f'Ну я же просил ввести ФИО кирилицей.\nПопробуй еще разок.')
    else:
        # for w in text.lower().split():
        #     r += ''.join([dct[ch] for ch in w if ch not in punctuation]).capitalize()
        # text = ' '.join(r)
        text = ' '.join([''.join([dct[ch] for ch in w if ch not in punctuation]).capitalize() for w in text.lower().split()])
        logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
        await bot.send_message(user_id, text)
        await bot.send_animation(message.chat.id,r'https://media.tenor.com/U22gcsK9bnQAAAAC/%D0%BB%D0%B0%D0%BF%D0%B5%D0%BD%D0%BA%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8%D0%BB%D0%B0%D0%BF%D0%B5%D0%BD%D0%BA%D0%BE.gif')

# if __name__ == '__mail__':
#     Dispatcher.start_polling(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())