from aiogram import types
from loader import dp

@dp.message_handler()
async def command_start(message: types.Message):
  await message.answer(f'Команда не найдена \n'
                      f'Воспользуйся командой /help\n'
                      f'Она расскажет обо всех возможных командах')
  