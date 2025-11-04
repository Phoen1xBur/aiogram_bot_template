from aiogram import Router
from aiogram.enums import ChatType

from utils.filters import ChatTypeFilter

router = Router(name=__name__)
router.message.filter(
    ChatTypeFilter(
        ChatType.GROUP,
    )
)