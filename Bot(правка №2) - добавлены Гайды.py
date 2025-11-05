import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot("") 

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, f"Приветствую в боте минипекки, это копия бота была создана для тренировки и оттачивания навыков")

@bot.message_handler(commands = ["test"])  #стартовая команда со всеми кнопками
def test_first_buttons(message):
  markup = types.InlineKeyboardMarkup(row_width=2)
  buttons = [
    types.InlineKeyboardButton("Пауэрлифтинг и силовые", callback_data="tab1"),
    types.InlineKeyboardButton("Бодибилдинг", callback_data="tab2"),
    types.InlineKeyboardButton("Авторы", callback_data="tab3"),
    types.InlineKeyboardButton("Рандомная тренеровка", callback_data="tab4"),
    types.InlineKeyboardButton("Гайды", callback_data="tab5")
  ]
  
  for button in buttons:
    markup.add(button) #добавляем все кнопки в масив markup

  bot.send_message(message.chat.id, "Выбери програму:", reply_markup=markup)



@bot.callback_query_handler(func=lambda call:call.data.startswith ("tab")) #тут проходит проверка нажата ли кнопка с началом tab
def handle_tabs(call): #получение номера вкладки
  tab_number = call.data.replace("tab","")  # замена название, то есть если было tab1 то станет просто 1, заменяем tab на пустоту

  tabs_content = {
        "1": "Пауэрлифтинг и силовые\n\nВыберите уровень подготовки:",
        "2": "Бодибилдинг\n\nВыберите пол:",
        "3": "Авторы\n\nИнформация о создателях бота",
        "4": "Рандомная тренировка\n\nВыберете сложность: ",
        "5": "Гайды\n\nВыберите руководство:"
    }

  tabs_buttons = {                      #Каждая кнопка - это список [текст_кнопки, callback_data]
    "1" : [["Начальный", "power_easy"],
          ["Средний", "power_normal"],
          ["Продвинутый уровень","power_advanced"],
          ["Назад в меню", "back_menu"]],
    "2" : [["Мужчина","gender_man"],
           ["Женщина","gender_woman"],
           ["Назад в меню", "back_menu"]],
    "3" : [["О команде","about_team"],
           ["Авторы","about_creators"],
           ["Назад в меню", "back_menu"]],
    "4" : [["Легкая","difficulty_easy"],
           ["Средняя","difficulty_normal"],
           ["Тяжелая","difficulty_hard"],
           ["Назад в меню", "back_menu"]],
    "5" : [["МАССОНАБОРНЫЙ ГАЙД","https://telegra.ph/Hh-06-01-10"],
           ["ГАЙД НА РЕКОМПОЗИЦИЮ","https://telegra.ph/Rekompoziciya-sushka-12-09"],
           ["ПРОГРЕСС - ЭТО НЕ СКУЧНО","https://telegra.ph/Progress---ehto-ne-skuchno-s-07-09"],
           ["ИЗБЕГАЕМ ТРАВМЫ","https://telegra.ph/Testovyj-dokument-07-09"],
           ["СПОРТПИТ","https://telegra.ph/Sport-pit-07-09"],
           ["ОБЩЕСУСТАВНАЯ РАЗМИНКА(txt)","guide_warm_up_txt"],
           ["ОБЩЕСУСТАВНАЯ РАЗМИНКА(video)","guide_warm_up_video"],
           ["Назад в меню", "back_menu"]]
  }

  tabs_choose_gender = {

  }

  markup = types.InlineKeyboardMarkup(row_width=2)
  for button_text,callback_data in tabs_buttons[tab_number]:
    if callback_data.startswith("http"):
            button = types.InlineKeyboardButton(button_text, url=callback_data)
    else:
            button = types.InlineKeyboardButton(button_text, callback_data=callback_data)
    markup.add(button)
  bot.edit_message_text(
    chat_id=call.message.chat.id, #указывают какое именно сообщение редактировать
    message_id=call.message.message_id,#указывают какое именно сообщение редактировать
    text=tabs_content[tab_number],#новый текст сообщения
    reply_markup=markup#новые кнопки под сообщением
  ) 
  bot.answer_callback_query(call.id) #Подтверждение нажатия

#@bot.callback_query_handler(func=lambda call:call.data.startswith ("power"))#надо доделать‼️

#@bot.callback_query_handler(func=lambda call:call.data.startswith ("gender"))#надо доделать‼️

#@bot.callback_query_handler(func=lambda call:call.data.startswith ("about"))#надо доделать‼️

#@bot.callback_query_handler(func=lambda call:call.data.startswith ("difficulty"))#надо доделать‼️

@bot.callback_query_handler(func=lambda call:call.data.startswith ("guide"))#надо доделать‼️
def send_guide_files(call):
    if call.data == "guide_warm_up_txt":
        file_path = "C:/Users/Admin/Desktop/Бот мини пекки/гайды/digestive_health_article.docx"  # путь к txt-файлу
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                bot.send_document(call.message.chat.id, f, caption="ОБЩЕСУСТАВНАЯ РАЗМИНКА (текст)")
        else:
            bot.send_message(call.message.chat.id, "Файл digestive_health_article.docx не найден ❌")

    elif call.data == "guide_warm_up_video":
        file_path = "C:/Users/Admin/Desktop/Бот мини пекки/гайды/joint_warm_up.mp4"  # путь видеофайлу
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                bot.send_video(call.message.chat.id, f, caption="ОБЩЕСУСТАВНАЯ РАЗМИНКА (видео)")
        else:
            bot.send_message(call.message.chat.id, "Видео joint_warm_up.mp4 не найдено ❌")

    bot.answer_callback_query(call.id)



@bot.callback_query_handler(func=lambda call:call.data == "back_menu")
def back_menu(call):
  markup = types.InlineKeyboardMarkup(row_width=2)
  buttons = [
    types.InlineKeyboardButton("Пауэрлифтинг и силовые", callback_data="tab1"),
    types.InlineKeyboardButton("Бодибилдинг", callback_data="tab2"),
    types.InlineKeyboardButton("Авторы", callback_data="tab3"),
    types.InlineKeyboardButton("Рандомная тренеровка", callback_data="tab4"),
    types.InlineKeyboardButton("Гайды", callback_data="tab5")
  ]

  for button in buttons:
    markup.add(button)

  bot.edit_message_text(
    chat_id=call.message.chat.id, 
    message_id=call.message.message_id,#
    text="Выберете опцию: ",
    reply_markup=markup
  )
  bot.answer_callback_query(call.id)

bot.polling(non_stop=True)