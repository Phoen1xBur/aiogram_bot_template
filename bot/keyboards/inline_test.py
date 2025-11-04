from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def inline_test(another_names: list[str]) -> InlineKeyboardMarkup:
    if not another_names:
        another_names = ['one', 'two', 'three']

    rows = [
        [InlineKeyboardButton(text='first row')],
        [InlineKeyboardButton(text=name) for name in another_names],
        [InlineKeyboardButton(text='third row')],
    ]

    return InlineKeyboardMarkup(
        inline_keyboard=rows,
    )
