from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from kafka import KafkaProducer, KafkaConsumer

from loader import dp

from states import reading

producer_tosend = KafkaProducer(bootstrap_servers='localhost:9092')
consumer_toget = KafkaConsumer('quickstart-events1',bootstrap_servers='localhost:9092')

@dp.message_handler(Command('go'))

async def go(message: types.Message):
  await message.answer('Поздравляю, ты начал процедуру генерации анекдотов\nТеперь на каждое твое сообщение бот постарается ответить тебе так, чтобы получился анекдот\n')
  await reading.test1.set()

@dp.message_handler(state=register.test1)

async def state1(message: types.Message, state: FSMContext):
  answer = message.text

  await state.update_data(test1=answer)
  await reading.test2.set()

@dp.message_handler(state=reading.test2)

async def state2(message: types.Message, state: FSMContext):
  answer = message.text
  await state.update_data(test2=answer)
  data = await state.get_data()
  first = data.get('test1')
  second = data.get('test2')

  await message.answer(f'Первое - {first}, второе - {second}\n')
