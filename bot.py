import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id
import json
from parcing_habr import chek_new_news
from aiogram.dispatcher.filters import Text
import asyncio
from parcing_postnauka import get_content



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Включаем логгирование что бы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# ПОЛУЧЕНИЕ КЛЮЧЕЙ ИЗ СЛОВАРЯ ПОСТНАУКИ ДЛЯ КНОПОК
list_keys_courses_dict = []
for k in get_content():
    list_keys_courses_dict.append(k)
    
#ФАЙЛ JSON 
with open('postnauka_dict.json', encoding='utf-8') as file:
        dict_postnauka = json.load(file)



# ФУНКЦИЯ ОТОБРАЖЕНИЯ КЛАВИАТУРЫ
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    buttons = ["Все новости из Habr", 'Последние 5 новостей из Habr', 'Свежие новости из Habr', 'Курсы Postnauka']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer('Лента статьей', reply_markup=keyboard)


# ВЫВОДИТ НОВОСТИ ИЗ СЛОВАРЯ Habr
@dp.message_handler(Text(equals="Все новости из Habr"))
async def get_news(message: types.Message):
    with open('new_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        new = f'<b>{v["article_date"]}</b>\n' \
              f'{v["article_url"]}'

        await message.answer(new)


# ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ПОСЛЕДНИХ НОВОСТЕЙ Habr
@dp.message_handler(Text(equals="Последние 5 новостей из Habr"))
async def get_last_news(message: types.Message):
    with open('new_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5::]:
        new = f'<b>{v["article_date"]}</b>\n' \
              f'{v["article_url"]}'

        await message.answer(new)


# ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ТОЛЬКО СВЕЖИХ НОВОСТЕЙ Habr
@dp.message_handler(Text(equals="Свежие новости из Habr"))
async def fresh_news(message: types.Message):
    fresh_news = chek_new_news()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items())[-5::]:
            new = f'<b>{v["article_date"]}</b>\n' \
                  f'{v["article_url"]}'
            await message.answer(new)
    else:
        await message.answer("На данный момент нет новых новостей...")


# ФУНКЦИЯ ПРОВЕРКИ НА НАЛИЧИЕ НОВЫХ НОВОСТЕ И ОТПРАВКИ В ЧАТ Habr
async def news_every_3minutes():
    while True:
        fresh_news = chek_new_news()
        if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items())[-5::]:
                new = f'<b>{v["article_date"]}</b>\n' \
                      f'{v["article_url"]}'

                await bot.send_message(user_id, new, disable_notification=True)

        await asyncio.sleep(900)


# ОТОБРАЖЕНИЕ КНОПОК С НАЗВАНИЕМ КУРСОВ НА Postnauka
@dp.message_handler(Text(equals='Курсы Postnauka'))
async def postnauka(message: types.Message):
    keyboard_courses_names = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_courses_names.add(*list_keys_courses_dict)
    await message.answer('Курсы Postnauka', reply_markup=keyboard_courses_names)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[0]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[0]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[0]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[0]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[1]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[1]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[1]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[1]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[2]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[2]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[2]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[2]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[3]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[3]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[3]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[3]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[4]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[4]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[4]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[4]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[5]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[5]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[5]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[5]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[6]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[6]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[6]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[6]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[7]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[7]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[7]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[7]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[8]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[8]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[8]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[8]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[9]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[9]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[9]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[9]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[10]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[10]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[10]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[10]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


#ОТОБРАЖЕНИЕ МАТЕРИАЛА С КУРСА ПОСЛЕ НАЖАТИЯ КНОПКИ С НАЗВАНИЕМ КУРСА
@dp.message_handler(Text(equals=list_keys_courses_dict[11]))
async def course1(message: types.Message):
    
    info = f"{dict_postnauka[list_keys_courses_dict[11]]['NAME_COURSE']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[11]]['URL']}\n" \
           f"{dict_postnauka[list_keys_courses_dict[11]]['NUMBER_VIDEO']}\n" 
        
    await message.answer(info)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_3minutes())
    executor.start_polling(dp, skip_updates=True)

