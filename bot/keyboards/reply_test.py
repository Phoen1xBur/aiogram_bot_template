from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def reply_test(another_names: list[str]) -> ReplyKeyboardMarkup:
    if not another_names:
        another_names = ['one', 'two', 'three']

    rows = [
        [KeyboardButton(text='first row')],
        [KeyboardButton(text=name) for name in another_names],
        [KeyboardButton(text='third row')],
    ]

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=rows,
        one_time_keyboard=True,
    )
