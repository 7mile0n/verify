**Overview**

**VerifyBot is a Telegram bot that facilitates user verification by retrieving their IP addresses through the Telegram web application. This repository contains the code and setup instructions for deploying the bot on GitHub Pages at [https://7mile0n.github.io/verify/].**

**Features**

- User verification through a web application.
- IP address retrieval and display in the chat.
- Simple and quick setup.

**Titles for the Repository**

- Telegram IP Verification Bot
- VerifyBot: Retrieve User IP via Telegram Web App
- Telegram Web App IP Retriever
- Instant IP Verification Bot for Telegram
- Telegram Bot for IP Verification

![image](https://github.com/7mile0n/verify/assets/144795540/53c61e56-5c2b-4072-8313-c8670f4af7d9)

**Example of Usage**
Prerequisites

- Python 3.7+
- aiogram library
- Telegram Bot API Token

```
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
  await start(web_app_message)

executor.start_polling(dp)
```
