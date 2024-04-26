import datetime
import re

name_pattern = '^[A-zА-я]{2,20}(-[A-zА-я]{2,10})?$'
phone_pattern = r'^\+373\d{8}$'
birthday_pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|19[789][0-9]|200[0-7])$'
email_pattern = r'^[A-Za-z0-9._-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$'
position_pattern = '^[A-zА-я]{4,20}$'


class Employee:
    def __init__(self, name, phone, birthday, email, position):
        self._name = None
        self._phone = None
        self._birthday = None
        self._email = None
        self._position = None
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.email = email
        self.position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not re.match(name_pattern, value):
            print("Некорректное имя. Имя должно быть от 2 до 20 букв и может содержать дефис.")
        else:
            self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not re.match(phone_pattern, value):
            print("Некорректный телефон. Формат телефона: +373xxxxxxxx.")
        else:
            self._phone = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if not re.match(birthday_pattern, value):
            print("Некорректная дата рождения. Формат даты: дд.мм.гггг, годы 1960-2007.")
        else:
            self._birthday = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(email_pattern, value):
            print("Некорректный email. Пример правильного формата: example@mail.com.")
        else:
            self._email = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not re.match(position_pattern, value):
            print("Некорректная специальность. Специальность должна быть от 4 до 20 букв.")
        else:
            self._position = value

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, position)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value <= 0:
            print("Часовая ставка должна быть положительным числом.")
        else:
            self._hourly_rate = value

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            print("Количество отработанных часов не может быть отрицательным.")
        else:
            self._hours_worked = value

    def _calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, monthly_salary):
        super().__init__(name, phone, birthday, email, position)
        self.monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if value <= 0:
            print("Месячная зарплата должна быть положительной суммой.")
        else:
            self._monthly_salary = value

    def _calculate_salary(self):
        return self.monthly_salary
