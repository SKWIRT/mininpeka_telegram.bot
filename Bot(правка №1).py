import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot("7839595192:AAGYba-TEtojuH77PheVwMN-281U6aodwkY")

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
    "5" : [["МАССОНАБОРНЫЙ ГАЙД","guide_mass_gain"],
           ["ГАЙД НА РЕКОМПОЗИЦИЮ","guide_recomposition"],
           ["ПРОГРЕСС - ЭТО НЕ СКУЧНО","guide_progress_not_bored"],
           ["ИЗБЕГАЕМ ТРАВМЫ","guide_injury"],
           ["СПОРТПИТ","guide_sport_nutrition"],
           ["ОБЩЕСУСТАВНАЯ РАЗМИНКА(txt)","guide_warm_up_txt"],
           ["ОБЩЕСУСТАВНАЯ РАЗМИНКА(video)","guide_warm_up_video"],
           ["Назад в меню", "back_menu"]]
  }

  tabs_choose_gender = {

  }

  markup = types.InlineKeyboardMarkup(row_width=2)
  for button_text,callback_data in tabs_buttons[tab_number]:
    button = types.InlineKeyboardButton(button_text,callback_data=callback_data)
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

#@bot.callback_query_handler(func=lambda call:call.data.startswith ("guide"))#надо доделать‼️

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