from aiogram import types, executor, Dispatcher, Bot
from main import print_info, print_img
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Привет, веди цифру')


@dp.message_handler()
async def welcome(message: types.Message):
    await message.answer(print_info(int(message.text)))
    photo = str(print_img(int(message.text)))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
