import os
from datetime import datetime, timedelta
import telebot
from telebot import types

API_TOKEN = '7140927526:AAF1VsOiFKO2P0Xsk0Sl6F4A4IxDQGZn8c8'

bot = telebot.TeleBot(API_TOKEN)

# Маппинг английских названий дней недели на русский
day_translation = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"
}


def load_schedule(filename):
    schedule = {'even_weeks': {}, 'odd_weeks': {}}
    with open(filename, 'r') as file:
        lines = file.readlines()
        current_week = None
        current_day = None
        for line in lines:
            line = line.strip()
            if line.endswith(':'):
                if line.startswith('even_weeks') or line.startswith('odd_weeks'):
                    current_week = line[:-1]
                else:
                    current_day = line[:-1]
                    schedule[current_week][current_day] = []
            elif line:
                parts = line.split(', ')
                if len(parts) == 5:
                    class_info = {
                        'number': int(parts[0]),
                        'time': parts[1],
                        'subject': parts[2],
                        'room': parts[3],
                        'teacher': parts[4]
                    }
                    schedule[current_week][current_day].append(class_info)
                else:
                    print(f'Предупреждение: Неверный формат класса в строке: "{line}"')
    return schedule


def get_week_type(date):
    week_number = date.isocalendar()[1]
    return 'even_weeks' if week_number % 2 == 0 else 'odd_weeks'


def get_week_type_message(date):
    week_number = date.isocalendar()[1]
    return 'Четная неделя' if week_number % 2 == 0 else 'Нечетная неделя'


def get_schedule_for_day(schedule, date):
    week_type = get_week_type(date)
    day_name = date.strftime('%A')
    return schedule.get(week_type, {}).get(day_name, [])


def get_schedule_for_range(schedule, start_date, end_date):
    current_date = start_date
    all_classes = []
    while current_date <= end_date:
        day_classes = get_schedule_for_day(schedule, current_date)
        all_classes.append((current_date.strftime('%A'), current_date.strftime('%d.%m.%Y'), day_classes))
        current_date += timedelta(days=1)
    return all_classes


def format_schedule(schedule, week_type_message):
    result = f'{week_type_message}\n\n'
    for day, date_str, classes in schedule:
        day_translated = day_translation.get(day, day)
        result += f'📅 {day_translated}, {date_str}:\n'
        for cls in classes:
            result += f'  ⏰ {cls["time"]} - {cls["subject"]}\n  Где: {cls["room"]}\n  с кем: {cls["teacher"]}\n\n'
        if not classes:
            result += '  Занятий нет\n'
        result += '\n'
    return result


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Введите название группы и подгруппы (если есть), например: I2302 1')


@bot.message_handler(func=lambda message: 'group' not in bot.user_data.get(message.from_user.id, {}))
def handle_group(message):
    group_input = message.text
    parts = group_input.split()
    if len(parts) == 1:
        group = parts[0]
        subgroup = None
    elif len(parts) == 2:
        group = parts[0]
        subgroup = parts[1]
    else:
        bot.reply_to(message, 'Неверный формат ввода.')
        return

    full_group = f'{group}_{subgroup}' if subgroup else group
    filename = f'{full_group}.txt'

    if not os.path.exists(filename):
        bot.reply_to(message, 'Файл расписания не найден.')
        return

    bot.user_data[message.from_user.id] = {'group': full_group}
    bot.send_message(message.chat.id, 'Выберите расписание:', reply_markup=generate_markup())


def generate_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('Сегодня'), types.KeyboardButton('Завтра'))
    markup.row(types.KeyboardButton('Эта неделя'), types.KeyboardButton('Следующая неделя'))
    return markup


@bot.message_handler(func=lambda message: message.text in ['Сегодня', 'Завтра', 'Эта неделя', 'Следующая неделя'])
def handle_option(message):
    option = message.text.lower()
    user_data = bot.user_data.get(message.from_user.id)

    if not user_data or 'group' not in user_data:
        bot.reply_to(message, 'Пожалуйста, сначала введите название группы.')
        return

    full_group = user_data['group']
    filename = f'{full_group}.txt'

    schedule = load_schedule(filename)
    today = datetime.today()
    if option == 'сегодня':
        schedule_to_print = get_schedule_for_range(schedule, today, today)
    elif option == 'завтра':
        tomorrow = today + timedelta(days=1)
        schedule_to_print = get_schedule_for_range(schedule, tomorrow, tomorrow)
    elif option == 'эта неделя':
        end_of_week = today + timedelta(days=(6 - today.weekday()))
        schedule_to_print = get_schedule_for_range(schedule, today, end_of_week)
    elif option == 'следующая неделя':
        start_of_next_week = today + timedelta(days=(7 - today.weekday()))
        end_of_next_week = start_of_next_week + timedelta(days=6)
        schedule_to_print = get_schedule_for_range(schedule, start_of_next_week, end_of_next_week)
    else:
        bot.reply_to(message, 'Неверный вариант.')
        return

    week_type_message = get_week_type_message(today)
    schedule_text = format_schedule(schedule_to_print, week_type_message)
    bot.send_message(message.chat.id, schedule_text)


# Хранение пользовательских данных
bot.user_data = {}

bot.polling()
