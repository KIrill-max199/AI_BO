from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from generators import generate
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловть в "AI_BOT"')


@router.message()
async def ai(message: Message):
    res = await generate(message.text)
    print(res.choices[0].message.content)
    await message.answer(res.choices[0].message.content)