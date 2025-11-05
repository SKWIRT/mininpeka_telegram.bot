import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot("8338749605:AAFWtwlJlmGSMMNguhzleuorUAz1Qd2ixoo") 

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
    "2" : [["🧔🏻Мужчина","gender_man"],
           ["👩🏻‍🦱Женщина","gender_woman"],
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

# Обработчик для вкладки "Авторы"
@bot.callback_query_handler(func=lambda call: call.data.startswith("about_"))
def handle_about(call):
    if call.data == "about_team":
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("⬅️ Назад", callback_data="tab3")
        markup.add(back_button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="новая амбициозная команда которая начала свой путь в разработке",
            reply_markup=markup
        )
    
    elif call.data == "about_creators":
        markup = types.InlineKeyboardMarkup(row_width=1)
        creator1 = types.InlineKeyboardButton("@dkdfdkd", url="https://t.me/dkdfdkd")
        creator2 = types.InlineKeyboardButton("@KaiiDoxxx", url="https://t.me/KaiiDoxxx")
        back_button = types.InlineKeyboardButton("⬅️ Назад", callback_data="tab3")
        markup.add(creator1, creator2, back_button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="👨‍💻 Создатели бота:\n\nСвяжитесь с нами:",
            reply_markup=markup
        )
    
    bot.answer_callback_query(call.id)

# Обработчик для рандомной тренировки
@bot.callback_query_handler(func=lambda call: call.data.startswith("difficulty_"))
def handle_random_training(call):
    # Собираем все возможные файлы из всех папок
    all_files = []
    
    # Папки для поиска файлов
    folders_to_search = [
        "C:/Users/Admin/Desktop/Бот мини пекки/программы/мужчины/",
        "C:/Users/Admin/Desktop/Бот мини пекки/программы/женщины/",
        "C:/Users/Admin/Desktop/Бот мини пекки/программы/мужчины/БезСпец/",
        "C:/Users/Admin/Desktop/Бот мини пекки/программы/женщины/БезСпец/",
        "C:/Users/Admin/Desktop/Бот мини пекки/гайды/"
    ]
    
    # Ищем все файлы в указанных папках
    for folder in folders_to_search:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(('.txt', '.docx', '.mp4')):
                    all_files.append(os.path.join(folder, file))
    
    # Выбираем случайный файл
    if all_files:
        random_file = random.choice(all_files)
        
        # Определяем тип файла и отправляем
        if random_file.endswith('.mp4'):
            with open(random_file, "rb") as f:
                bot.send_video(call.message.chat.id, f, caption="🎲 Случайная тренировка!")
        else:
            with open(random_file, "rb") as f:
                bot.send_document(call.message.chat.id, f, caption="🎲 Случайная тренировка!")
    else:
        bot.send_message(call.message.chat.id, "❌ Файлы с программами не найдены")
    
    # Кнопка для возврата
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("⬅️ Назад к выбору сложности", callback_data="tab4")
    markup.add(back_button)
    
    bot.send_message(
        chat_id=call.message.chat.id,
        text="🎲 Вот ваша случайная тренировка!",
        reply_markup=markup
    )
    
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data in ["gender_man", "gender_woman"])
def handle_gender_selection(call):
    gender = "🧔🏻Мужчина" if call.data == "gender_man" else "👩🏻‍🦱Женщина"
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("🟢Меньше года", callback_data=f"experience_less_{call.data}"),
        types.InlineKeyboardButton("🟡1-3 года", callback_data=f"experience_1-3_{call.data}"),
        types.InlineKeyboardButton("🔴Больше 3 лет", callback_data=f"experience_more3_{call.data}"),
        types.InlineKeyboardButton("Назад", callback_data="tab2")
    ]
    
    for button in buttons:
        markup.add(button)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"{gender}\n\nВыберите ваш стаж тренировок:",
        reply_markup=markup
    )
    bot.answer_callback_query(call.id)

# Обработчик для выбора стажа
@bot.callback_query_handler(func=lambda call: call.data.startswith("experience_"))
def handle_experience_selection(call):
    parts = call.data.split("_")
    experience = parts[1]
    gender = parts[2] + "_" + parts[3]  # gender_man или gender_woman
    
    experience_texts = {
        "less": "🟢Меньше года",
        "1-3": "🟡1-3 года", 
        "more3": "🔴Больше 3 лет"
    }
    
    if experience == "less":
        # Для стажа меньше года - сразу выбор графика
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("🐘2x2", callback_data=f"schedule_2-2_{gender}_{experience}"),
            types.InlineKeyboardButton("🦍3 дня", callback_data=f"schedule_3days_{gender}_{experience}"),
            types.InlineKeyboardButton("Назад", callback_data=f"{gender}")
        ]
        
        for button in buttons:
            markup.add(button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"🏋️ Стаж: {experience_texts[experience]}\n\nВыберите график тренировок:",
            reply_markup=markup
        )
    
    else:
        # Для стажа 1-3 года и больше 3 лет - сначала выбор специализации
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("Да", callback_data=f"specialization_yes_{gender}_{experience}"),
            types.InlineKeyboardButton("Нет", callback_data=f"specialization_no_{gender}_{experience}"),
            types.InlineKeyboardButton("Назад", callback_data=f"{gender}")
        ]
        
        for button in buttons:
            markup.add(button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"💪🏻Бодибилдинг\n\n— Выберите стаж: {experience_texts[experience]}\n\nНужна ли специализация?",
            reply_markup=markup
        )
    
    bot.answer_callback_query(call.id)

# Обработчик для выбора специализации
@bot.callback_query_handler(func=lambda call: call.data.startswith("specialization_"))
def handle_specialization_selection(call):
    parts = call.data.split("_")
    needs_specialization = parts[1]  # yes или no
    gender = parts[2] + "_" + parts[3]
    experience = parts[4]
    
    if needs_specialization == "no":
        # Если специализация не нужна - выбор графика
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("🐘2x2", callback_data=f"schedule_2-2_{gender}_{experience}"),
            types.InlineKeyboardButton("🦍3 дня", callback_data=f"schedule_3days_{gender}_{experience}"),
            types.InlineKeyboardButton("Назад", callback_data=f"experience_{experience}_{gender}")
        ]
        
        for button in buttons:
            markup.add(button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите график тренировок:",
            reply_markup=markup
        )
    
    else:
        # Если нужна специализация - выбор группы мышц
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("Спина", callback_data=f"muscle_back_{gender}_{experience}"),
            types.InlineKeyboardButton("Ноги", callback_data=f"muscle_legs_{gender}_{experience}"),
            types.InlineKeyboardButton("Руки", callback_data=f"muscle_arms_{gender}_{experience}"),
            types.InlineKeyboardButton("Грудь", callback_data=f"muscle_chest_{gender}_{experience}"),
            types.InlineKeyboardButton("Плечи", callback_data=f"muscle_shoulders_{gender}_{experience}"),
            types.InlineKeyboardButton("Грудь+Спина", callback_data=f"muscle_chest-back_{gender}_{experience}"),
            types.InlineKeyboardButton("Руки+Плечи", callback_data=f"muscle_arms-shoulders_{gender}_{experience}"),
            types.InlineKeyboardButton("Назад", callback_data=f"experience_{experience}_{gender}")
        ]
        
        for button in buttons:
            markup.add(button)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите специализацию:",
            reply_markup=markup
        )
    
    bot.answer_callback_query(call.id)

# Обработчик для выбора специализации
@bot.callback_query_handler(func=lambda call: call.data.startswith("muscle_"))
def handle_muscle_selection(call):
    parts = call.data.split("_")
    muscle_group = parts[1]
    gender = parts[2] + "_" + parts[3]
    experience = parts[4]
    
    # После выбора специализации - выбор графика
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("🐘2x2", callback_data=f"schedule_2-2_{gender}_{experience}_{muscle_group}"),
        types.InlineKeyboardButton("🦍3 дня", callback_data=f"schedule_3days_{gender}_{experience}_{muscle_group}"),
        types.InlineKeyboardButton("Назад", callback_data=f"specialization_yes_{gender}_{experience}")
    ]
    
    for button in buttons:
        markup.add(button)
    
    muscle_names = {
        "back": "Спина",
        "legs": "Ноги", 
        "arms": "Руки",
        "chest": "Грудь",
        "shoulders": "Плечи",
        "chest-back": "Грудь+Спина",
        "arms-shoulders": "Руки+Плечи"
    }
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"Специализация: {muscle_names[muscle_group]}\n\nВыберите график тренировок:",
        reply_markup=markup
    )
    bot.answer_callback_query(call.id)


# Обработчик выбора графика и отправки программы !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@bot.callback_query_handler(func=lambda call: call.data.startswith("schedule_"))
def handle_final_program(call):
    parts = call.data.split("_")
    schedule = parts[1]  # 2-2 или 3days
    gender = parts[2] + "_" + parts[3]
    experience = parts[4]
    muscle_group = parts[5] if len(parts) > 5 else None
    
    # Определяем тексты для разных параметров
    gender_text = "🧔🏻Мужчина" if gender == "gender_man" else "👩🏻‍🦱Женщина"
    gender_folder = "мужчины" if gender == "gender_man" else "женщины" #ОБЪЯЗАТЕЛЬНО В ПУТИ ДОЛЖНО БЫТЬ РАЗДЕЛЕНИЕ В ПАПКИ МУЖЧИН И ЖЕНЩИН
    
    experience_texts = {
        "less": "🟢Меньше года",
        "1-3": "🟡1-3 года",
        "more3": "🔴Больше 3 лет"
    }
    
    schedule_texts = {
        "2-2": "🐘2x2",
        "3days": "🦍3 дня"
    }
    
    muscle_names = {
        "back": "Спина",
        "legs": "Ноги",
        "arms": "Руки", 
        "chest": "Грудь",
        "shoulders": "Плечи",
        "chest-back": "Грудь+Спина",
        "arms-shoulders": "Руки+Плечи"
    }
    
    # Определяем путь к файлу в зависимости от пола, специализации И графика
    if muscle_group:
        # Есть специализация - используем файлы для конкретного пола, мышц и графика
        file_paths = {
            "back_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/спина_2x2.txt",
            "back_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/спина_3дня.txt",
            "legs_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/ноги_2x2.txt",
            "legs_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/ноги_3дня.txt",
            "arms_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/руки_2x2.txt",
            "arms_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/руки_3дня.txt",
            "chest_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/грудь_2x2.txt",
            "chest_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/грудь_3дня.txt",
            "shoulders_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/плечи_2x2.txt",
            "shoulders_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/плечи_3дня.txt",
            "chest-back_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/грудь_спина_2x2.txt",
            "chest-back_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/грудь_спина_3дня.txt",
            "arms-shoulders_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/руки_плечи_2x2.txt",
            "arms-shoulders_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/руки_плечи_3дня.txt"
        }
        file_key = f"{muscle_group}_{schedule}"
        file_path = file_paths.get(file_key)
        specialization_text = f"Специализация: Да"
        muscle_text = f"Группа мышц: {muscle_names[muscle_group]}"
    else:
        # Нет специализации - используем общие файлы по полу, стажу и графику
        file_paths = {
            "less_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/начинающий_2x2.txt",
            "less_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/начинающий_3дня.txt",
            "1-3_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/средний_2x2.txt",
            "1-3_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/средний_3дня.txt",
            "more3_2-2": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/продвинутый_2x2.txt",
            "more3_3days": f"C:/Users/Admin/Desktop/Бот мини пекки/программы/{gender_folder}/БезСпец/продвинутый_3дня.txt"
        }
        file_key = f"{experience}_{schedule}"
        file_path = file_paths.get(file_key)
        specialization_text = "Специализация: Нет"
        muscle_text = "Группа мышц: Общая программа"
    
    # Формируем текст для подписи
    caption = f"Тренировка\n\n" \
              f"Пол: {gender_text}\n" \
              f"Опыт: {experience_texts[experience]}\n" \
              f"График: {schedule_texts[schedule]}\n" \
              f"Специализация: {'Да' if muscle_group else 'Нет'}\n" \
              f"Группа мышц: {muscle_names[muscle_group] if muscle_group else 'Общая программа'}"
    
    # Отправляем файл
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            bot.send_document(call.message.chat.id, f, caption=caption)
    else:
        # Если файл не найден, отправляем сообщение
        bot.send_message(
            call.message.chat.id,
            f"❌ Файл с программой не найден\n\n{caption}\n\nПуть: {file_path}"
        )
    
    # Кнопка для возврата в меню
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("◀ Вернуться в меню", callback_data="back_menu")
    markup.add(back_button)
    
    bot.send_message(
        chat_id=call.message.chat.id,
        text="💪🏻 Бодибилдинг\n— Вот все программы, которые мне удалось найти. Приятной тренировки!",
        reply_markup=markup
    )
    
    bot.answer_callback_query(call.id)
    

@bot.callback_query_handler(func=lambda call:call.data.startswith ("guide"))
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