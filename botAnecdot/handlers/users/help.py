from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
  await message.answer(f'Ты можешь воспользоваться следующими командами:\n'
                      f'/start - выводит приветственное сообщение\n'
                      f'/help - то, что ты сейчас читаешь\n'
                      f'/go - запускает процедуру генерации анекдотов')
  