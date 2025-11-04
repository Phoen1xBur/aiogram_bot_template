# run.py
import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import settings



# Логирование
logger = logging.getLogger(__name__)

# Инициализация бота и клиента
bot = Bot(token=settings.TOKEN)
dp = Dispatcher()


async def start_bot():
    """Запуск Telegram бота"""
    from handlers import routers
    from middleware import middlewares

    dp.include_routers(*routers)

    for middleware in middlewares:
        dp.update.middleware(middleware)

    bot.default.parse_mode = 'HTML'

    # Запуск polling
    await dp.start_polling(bot)


async def on_startup():
    """Запуск всех сервисов"""
    # Создаем задачи для бота и API
    task_list = [
        asyncio.create_task(start_bot()),  # bot_task
    ]

    # Ждем завершения всех задач
    await asyncio.gather(*task_list)


if __name__ == '__main__':
    try:
        asyncio.run(on_startup())
    except KeyboardInterrupt:
        logger.info('Остановка...')
    except Exception as e:
        logger.exception('Необработанная ошибка: %s', e)
