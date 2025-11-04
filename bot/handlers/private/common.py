from aiogram import Router, Bot, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.filters import ChatTypeFilter, WordFilter

router = Router(name=__name__)
router.message.filter(
    ChatTypeFilter(
        ChatType.PRIVATE,
    )
)

@router.message(CommandStart())
async def start(message: Message):
    await message.reply('Привет! Меня зовут Вася! Приятно познакомиться!')


@router.message(
    WordFilter(
        words=('Вася', 'Василий'),
        ignore_case=True,
    ),
    (F.text[0] != '/')
)
async def answer_by_bot_name(message: Message, bot: Bot):
    await message.reply('Привет! Да, это мое имя!')


@router.message(
    (F.text[0] != '/')
)
async def echo(message: Message):
    await message.reply(message.text)