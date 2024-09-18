import random
import asyncio,telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.handler_backends import StatesGroup, State

bot_token = "TELEGRAM_BOT_TOKEN"
bot = AsyncTeleBot(bot_token)


@bot.message_handler(content_types=['text'])
async def respond_to_me(message):
    try:
        # extract message sent by user
        user_message = message.text
        message_to_send = f"this is your message:\n{user_message}"
        # respond to user
        await bot.reply_to(message,message_to_send)
    except Exception as me:
        print("respond_to_me:", me)

asyncio.run(bot.polling())        
        