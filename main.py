import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from database import init_db
from handlers import user_handlers, admin_handlers

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для инициализации всех обработчиков и запуска бота
async def main():
    # Инициализация базы данных
    init_db()

    # Регистрация обработчиков
    user_handlers.register_handlers(dp, bot)
    admin_handlers.register_handlers(dp, bot)

    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен...")
    asyncio.run(main())
