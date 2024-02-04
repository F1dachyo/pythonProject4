import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os


TOKEN = "6625335218:AAHvncUcXU5f278db8MRv_uiC88EkzkbgmM"


bot = Bot(token=TOKEN)
dp = Dispatcher()


def restart_pc():
    os.system("shutdown /r /t 0")


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Бот работает!")


@dp.message(Command("ddos"))
async def process_help_command(message: types.Message):
    await message.reply("Выключаю компьютер!")
    restart_pc()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())