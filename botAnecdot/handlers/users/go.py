from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import register

@dp.message_handler(Command('go'))

async def go(message: types.Message):
  await message.answer('Поздравляю, ты начал процедуру генерации анекдотов\nТеперь на каждое твое сообщение бот постарается ответить тебе так, чтобы получился анекдот\n')
  await register.test1.set()

@dp.message_handler(state=register.test1)

async def state1(message: types.Message, state: FSMContext):
  answer = message.text

  await state.update_data(test1=answer)
  await register.test2.set()

@dp.message_handler(state=register.test2)

async def state2(message: types.Message, state: FSMContext):
  answer = message.text
  await state.update_data(test2=answer)
  data = await state.get_data()
  first = data.get('test1')
  second = data.get('test2')

  await message.answer(f'Первое - {first}, второе - {second}\n')