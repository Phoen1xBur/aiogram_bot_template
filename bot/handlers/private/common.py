from aiogram import Router, Bot, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from utils.filters import ChatTypeFilter, WordFilter
from keyboards import reply_test, inline_test

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


@router.message(Command('reply_keyboard'))
async def reply_keyboard(message: Message, bot: Bot):
    await message.reply(text='reply_keyboard', reply_markup=reply_test.reply_test(['One', 'Two', 'Three']))


@router.message(Command('inline_keyboard'))
async def inline_keyboard(message: Message, bot: Bot):
    await message.reply(text='inline_keyboard', reply_markup=inline_test.inline_test(['one', 'two', 'three']))


@router.message(
    (F.text[0] != '/')
)
async def echo(message: Message, bot: Bot):
    await message.reply(message.text)