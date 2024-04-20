from datetime import datetime
import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        # Устанавливаем начальные значения только если они проходят валидацию
        self.set_name(name)
        self.set_phone(phone)
        self.set_birthday(birthday)
        self.set_email(email)
        self.set_specialty(specialty)

    def calculateAge(self):
        if hasattr(self, '_Employee__birthday'):
            today = datetime.now()
            birthday_date = datetime.strptime(self._Employee__birthday, "%d.%m.%Y")
            age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
            return age
        else:
            print("Дата рождения не установлена.")
            return None

    def _calculateSalary(self):
        pass  # Этот метод должен быть переопределен в подклассах

    def set_name(self, value):
        if re.match(r'^[A-zА-я]+$', value):
            self.__name = value
        else:
            print("Имя должно содержать только буквы.")

    def set_phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self.__phone = value
        else:
            print("Номер телефона должен соответствовать формату +373 и содержать 8 цифр.")

    def set_birthday(self, value):
        if re.match(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(1960|19[7-9]\d|200[0-7])$', value):
            self.__birthday = value
        else:
            print("Дата рождения должна быть в формате ДД.ММ.ГГГГ, год должен быть между 1960 и 2007.")

    def set_email(self, value):
        if re.match(r'^[\w.-]{2,20}@\w{4,7}\.\w{2,4}$', value):
            self.__email = value
        else:
            print("Некорректный формат электронной почты.")

    def set_specialty(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self.__specialty = value
        else:
            print("Специальность должна состоять только из букв и быть длиной от 4 до 20 символов.")

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, specialty)
        self.set_hourly_rate(hourly_rate)
        self.set_hours_worked(hours_worked)

    def _calculateSalary(self):
        if hasattr(self, '_HourlyEmployee__hourly_rate') and hasattr(self, '_HourlyEmployee__hours_worked'):
            return self.__hourly_rate * self.__hours_worked
        else:
            print("Не установлены почасовая ставка или количество отработанных часов.")
            return None

    def set_hourly_rate(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self.__hourly_rate = float(value)
        else:
            print("Некорректная почасовая ставка. Введите правильное числовое значение.")

    def set_hours_worked(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self.__hours_worked = float(value)
        else:
            print("Некорректное количество отработанных часов. Введите правильное числовое значение.")

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthly_salary):
        super().__init__(name, phone, birthday, email, specialty)
        self.set_monthly_salary(monthly_salary)

    def _calculateSalary(self):
        if hasattr(self, '_SalaryEmployee__monthly_salary'):
            return self.__monthly_salary
        else:
            print("Месячная зарплата не установлена.")
            return None

    def set_monthly_salary(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self.__monthly_salary = float(value)
        else:
            print("Некорректная месячная зарплата. Введите правильное числовое значение.")