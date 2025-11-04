from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_test(another_names: list[str]) -> InlineKeyboardMarkup:
    if not another_names:
        another_names = ['one', 'two', 'three']

    """
    Особенность inline-клавиатуры в том, что она не может быть просто текстом.
    В ней должен быть либо url, либо какой то callback_data (функция, которую бот делает при нажатии на кнопку)
    Примечание: callback_data может быть не реализованна.
    """
    rows = [
        [InlineKeyboardButton(text='first row', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),],
        [InlineKeyboardButton(text=name, callback_data=name) for name in another_names],
        [InlineKeyboardButton(text='third row', callback_data='third')],
    ]

    return InlineKeyboardMarkup(
        inline_keyboard=rows,
    )
