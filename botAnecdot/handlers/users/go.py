import re

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

@dp.message_handler(state=reading.test1)

async def state1(message: types.Message, state: FSMContext):
  answer = message.text

  await state.update_data(test1=answer)
  await message.answer('Генерация займет некоторое время')
  text1 = await state.get_data('test1')
  key_bytes = bytes("123", encoding="utf-8")
  value_bytes = bytes(text1.get('text1'), encoding="utf-8") 
  producer_tosend.send('quickstart-events2', key=key_bytes, value=value_bytes) 
  producer_tosend.flush()
  for msg in consumer_toget:
      if (msg.key.decode("utf-8") == '333'):
         print (msg.value.decode("utf-8"))
         s = msg.value.decode("utf-8")
         generated_text = s.replace('[SJ]', '').split("[")[0]
         break
  await message.answer(generated_text)
  await state.finish()
