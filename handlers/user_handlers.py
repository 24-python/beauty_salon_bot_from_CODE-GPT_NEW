from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.user_keyboards import get_service_menu

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Добро пожаловать в наш салон красоты!", reply_markup=get_service_menu())

# Обработчик для записи на услугу (здесь фильтр по тексту)
@router.message(lambda message: message.text == "Записаться")
async def handle_booking(message: Message):
    await message.answer("Какую услугу вы хотите выбрать?")

# Функция для регистрации обработчиков
def register_handlers(dp, bot):
    dp.include_router(router)
