from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'здравья желаю {message.from_user.first_name}')

@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    await message.answer(text=f'Список команд: /start- используй для того что-бы начать разговор с ботом '
                              f' /myinfo-используя эту команду можешь узнать информацю о себе'
                              f' /picture-используя эту команду бот отправит тебе рандомную картинку из папки images')

@dp.message_handler(commands=['myinfo'])
async def start_handler(message: types.Message):
    await message.answer(text=f'Ваш id: {message.from_user.id}, '
                              f'Bаш nickname: {message.from_user.first_name} '
                              f'Ваш username: {message.from_user.username} ')
    await message.delete()


@dp.message_handler(commands=['picture'])
async def image_sender(message: types.Message):
    await message.answer_photo(
        open('67f069102446d07811d0d0243603e40d')
    )

    await message.delete()


@dp.message_handler()
async def kopirovatski(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':

    executor.start_polling(dp)

