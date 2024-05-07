import calendar
import re
import datetime


def day_of_week():

    date_pattern = r"(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"
    date_input = input("Введите дату в формате ГГГГ-ММ-ДД: ")

    if not re.match(date_pattern, date_input):
        print("Дата введена некорректно. Используйте формат ГГГГ-ММ-ДД.")
        return

    date = date_input.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    if datetime.date(year, month, day) > datetime.date.today():
        print("Дата рождения не может превышать сегодняшний день.")
        return

    week_day = calendar.weekday(year, month, day)

    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    print(f"День недели для даты {date_input}: {days[week_day]}")


day_of_week()
