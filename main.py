import asyncio
import requests
import logging
import sys
from aiogram.enums import ParseMode
from aiogram import Bot, types
import aiogram.utils
import config
from aiogram.filters import CommandStart

bot = Bot(token=config.TOKEN)
dp = aiogram.Dispatcher()

async def send_currency_rate(chat_id):
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        rate = str(data['Valute']['USD']['Value'])
        await bot.send_message(chat_id, rate)
    except requests.RequestException as e:
        print("Ошибка при отправке запроса к Центробанку:", e)

@dp.message(CommandStart())
async def start(message: types.Message):
    while True:
        try:
            await send_currency_rate(message.chat.id)
            await asyncio.sleep(5)
        except Exception as e:
            print("Ошибка при отправке сообщения:", e)

async def main():
    global dp
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
