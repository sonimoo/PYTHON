import datetime
import re


def calculate_age_in_days():
    date_pattern = "([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"

    today = datetime.date.today()

    date_input = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    if re.match(date_pattern, date_input):
        date = date_input.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        birth_date = datetime.date(year, month, day)

        if birth_date > today:
            print("Дата рождения не может превышать сегодняшний день.")
            return

        life = today - birth_date
        print(f"Ваш возраст в днях - {life.days}")
    else:
        print("Некорректная дата. (формат ГГГГ-ММ-ДД.")


calculate_age_in_days()
