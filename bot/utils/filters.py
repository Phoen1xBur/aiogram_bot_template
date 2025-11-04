from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.enums import ChatType, ContentType


class ChatTypeFilter(BaseFilter):
    def __init__(self, *chat_type: Union[ChatType, list[ChatType]]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if not isinstance(message, Message):
            return True
        if isinstance(self.chat_type, ChatType):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


class MessageTypeFilter(BaseFilter):
    def __init__(self, *message_type: Union[ContentType, list[ContentType]]):
        self.message_type = message_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.message_type, ContentType):
            return message.content_type == self.message_type
        else:
            return message.content_type in self.message_type


class WordFilter(BaseFilter):
    """Фильтр для проверки нахождения целых слов в сообщении."""

    def __init__(
            self,
            words: Union[str, tuple[str, ...], list[str]],
            ignore_case: bool = False,
    ):
        if isinstance(words, str):
            self.words = (words,)
        else:
            self.words = tuple(words)
        self.ignore_case = ignore_case

        if self.ignore_case:
            self.words = tuple(word.casefold() for word in self.words)

    async def __call__(self, message: Message) -> bool:
        try:
            if not message.text or not message.text.strip():
                return False

            # Разбиваем текст на слова
            if self.ignore_case:
                text_words = message.text.casefold().split()
            else:
                text_words = message.text.split()

            # Проверяем наличие слов из списка в тексте
            for word in self.words:
                if word in text_words:
                    return True

            return False

        except (AttributeError, TypeError):
            return False
