import logging
import os
import environ

from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
    
from aiogram import Bot,Dispatcher,executor,types

API_TOKEN = get_env_variable('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum! Men Something taomxonasining botiman. Nima xizmat, aylanay?")

@dp.message_handler()
async def response(message:types.Message):
    some_text = "ehehehe"
    await message.answer(some_text)

print("Crashing...")

if __name__ == '__main__':
    print("working...")
    executor.start_polling(dp, skip_updates=True)