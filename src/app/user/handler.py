from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.app.user.crud import UserService

router = Router()


@router.message(CommandStart())
async def start_message(message: Message):
    await UserService.add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        firstname=message.from_user.first_name,
        lastname=message.from_user.last_name,
    )

    await message.answer(text=f"You are in the database now")
