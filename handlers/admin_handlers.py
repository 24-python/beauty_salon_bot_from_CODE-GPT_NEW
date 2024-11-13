from aiogram import Router, types, Bot
from aiogram.filters import Command
from config import ADMIN_IDS

router = Router()

# Обработчик команды /admin (только для администраторов)
@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer("Добро пожаловать в панель администратора!")
    else:
        await message.answer("У вас нет доступа.")

# Функция для регистрации обработчиков
def register_handlers(dp, bot: Bot):
    dp.include_router(router)
