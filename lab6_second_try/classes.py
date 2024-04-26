import datetime
import re

name_pattern = '^[A-zА-я]{2,20}(-[A-zА-я]{2,10})?$'
phone_pattern = r'^\+373\d{8}$'
birthday_pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19[6789][0-9]|200[0-7])$'
email_pattern = r'^[A-Za-z0-9._-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$'
position_pattern = '^[A-zА-я]{4,20}$'


class Employee:
    def __init__(self, name, phone, birthday, email, position):
        self.__name = name
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__position = position
        self.set_name(name)
        self.set_phone(phone)
        self.set_birthday(birthday)
        self.set_email(email)
        self.set_position(position)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if not re.match(name_pattern, value):
            print("Некорректное имя. Имя должно быть от 2 до 20 букв и может содержать дефис.")
        else:
            self.__name = value

    name = property(get_name, set_name)

    def get_phone(self):
        return self.__phone

    def set_phone(self, value):
        if not re.match(phone_pattern, value):
            print("Некорректный телефон. Формат телефона: +373xxxxxxxx.")
        else:
            self.__phone = value

    phone = property(get_phone, set_phone)

    def get_birthday(self):
        return self.__birthday

    def set_birthday(self, value):
        if not re.match(birthday_pattern, value):
            print("Некорректная дата рождения. Формат даты: дд.мм.гггг, годы 1960-2007.")
        else:
            self.__birthday = value

    birthday = property(get_birthday, set_birthday)

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if not re.match(email_pattern, value):
            print("Некорректный email. Пример правильного формата: example@mail.com.")
        else:
            self.__email = value

    email = property(get_email, set_email)

    def get_position(self):
        return self.__position

    def set_position(self, value):
        if not re.match(position_pattern, value):
            print("Некорректная специальность. Специальность должна быть от 4 до 20 букв.")
        else:
            self.__position = value

    position = property(get_position, set_position)

    def calculate_age(self):
        birthdate = datetime.datetime.strptime(self.__birthday, "%d.%m.%Y")
        today = datetime.datetime.now()
        age = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1
        return age

    def _calculate_salary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, position)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def _calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, monthly_salary):
        super().__init__(name, phone, birthday, email, position)
        self.__monthly_salary = monthly_salary

    def _calculate_salary(self):
        return self.__monthly_salary
