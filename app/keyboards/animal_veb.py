from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_animal_veb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин на лікувані")
    builder.button(text="Додати нову тварину")
    builder.button(text="Показати список вилікуваних тварин")
    builder.button(text="Додати відгук")
    builder.button(text="Показати всі відгуки")
    builder.adjust(1)
    return builder.as_markup()