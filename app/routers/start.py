from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from app.keyboards.animal_veb import build_animal_veb 

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = build_animal_veb()
    text = (
        f"Вітаю, {hbold(message.from_user.full_name)}, в інформаційній системі ветеренарної клініки!\n"
        "\nВиберіть дію"
    )
    await message.answer(
        text=text,
        reply_markup=keyboard
    )