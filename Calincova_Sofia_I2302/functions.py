import re
import datetime

name_pattern = '^[A-zА-я]{2,20}(-[A-zА-я]{2,20})?$'
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(202[34])$'
grade_pattern = '^(10|[1-9])$'


def validate_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, '%d.%m.%Y')
        start_date = datetime.datetime(2023, 9, 1)
        current_date = datetime.datetime.now()
        return start_date <= date_obj <= current_date
    except ValueError:
        return False


def input_data():
    while True:
        surname = input("Введите фамилию ученика: ")
        if not re.match(name_pattern, surname):
            print("  Некорректная фамилия. Убедитесь, что фамилия написана правильно.")
            continue

        name = input("Введите имя ученика: ")
        if not re.match(name_pattern, name):
            print("  Некорректное имя. Убедитесь, что имя написано правильно.")
            continue

        date = input("Введите дату (дд.мм.гггг): ")
        if not re.match(date_pattern, date) or not validate_date(date):
            print("  Некорректная дата."
                  "\n  Дата должна быть в формате дд.мм.гггг и находиться в диапазоне с 01.09.2023 по текущий день."
                  "\n  Возможно вы указали неверное количество дней в месяце!")
            continue

        grade = input("Введите оценку (1-10): ")
        if not re.match(grade_pattern, grade):
            print("  Некорректная оценка. Оценка должна быть числом от 1 до 10.")
            continue

        # Форматирование данных для "таблицы"
        formatted_data = f"{surname:<30}\t{name:<30}\t{date:<15}\t{grade:<5}"
        with open("data.txt", mode='a', encoding='utf-8') as f:
            f.write(formatted_data + "\n")
        print("Данные успешно сохранены в файл data.txt.")
        break


def calculate_grade():
    with open("data.txt", mode="r", encoding='utf-8') as f:
        grades = [int(line.split()[-1]) for line in f.readlines() if line.strip()]
        if grades:
            average = sum(grades) / len(grades)
            print(f"Средняя оценка класса: {average:.2f}")
        else:
            print("Нет данных для расчета.")


def grades_below_5():
    with open("data.txt", mode="r", encoding='utf-8') as f:
        students = [line.strip().split()[:2] for line in f if int(line.split()[-1]) < 5]

        if not students:
            print("Учеников с оценками меньше 5 нет.")
        else:
            print("Список учеников с оценками меньше 5:")
            for student in students:
                print(' '.join(student))


def grades_above_8():
    with open("data.txt", mode="r", encoding='utf-8') as f:
        students = [line.strip().split()[:2] for line in f if int(line.split()[-1]) > 8]

        if not students:
            print("Учеников с оценками больше 8 нет.")
        else:
            print("Список учеников с оценками больше 8:")
            for student in students:
                surname, name = student
                print(f"{surname} {name}")
