from aiogram import Router, types, Bot
from aiogram.filters import Command, Text
from keyboards.user_keyboards import get_service_menu

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в наш салон красоты!", reply_markup=get_service_menu())

# Обработчик для записи на услугу
@router.message(Text("Записаться"))
async def handle_booking(message: types.Message):
    await message.answer("Какую услугу вы хотите выбрать?")

# Функция для регистрации обработчиков
def register_handlers(dp, bot: Bot):
    dp.include_router(router)
