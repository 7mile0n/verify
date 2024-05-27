from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(TOKEN, parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Verification',
                                  web_app=WebAppInfo(url='https://7mile0n.github.io/verify/'))]
        ],
        resize_keyboard=True
    )
    await bot.send_message(message.chat.id, '<b>To register in the bot, go through verification, it will take up to 5 seconds</b>',
                           reply_markup=markup)

@dp.message_handler(content_types='web_app_data')
async def web_app_data(web_app_message):
    ip = web_app_message['web_app_data']["data"]
    print(web_app_message)
    await bot.send_message(web_app_message.chat.id, f"Your ip: {ip}",
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(web_app_message.chat.id, "You have been successfully registered", reply_markup=types.ReplyKeyboardRemove())

executor.start_polling(dp)
