from datetime import datetime
import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__specialty = specialty

    def calculateAge(self):
        today = datetime.now()
        birthday_date = datetime.strptime(self.__birthday, "%d.%m.%Y")
        age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
        return age

    def _calculateSalary(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if re.match(r'^[a-zA-Z]+$', value):
            self.__name = value
        else:
            raise ValueError("Invalid name. Only letters are allowed.")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self.__phone = value
        else:
            raise ValueError("Phone number must match +373 followed by 8 digits.")

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if re.match(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(1960|19[7-9]\d|200[0-7])$', value):
            self.__birthday = value
        else:
            raise ValueError("Birthday must be in format DD.MM.YYYY and year between 1960 and 2007.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if re.match(r'^[\w.-]{2,20}@\w{4,7}\.\w{2,4}$', value):
            self.__email = value
        else:
            raise ValueError("Invalid email format.")

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self.__specialty = value
        else:
            raise ValueError("Specialty must be 4-20 letters.")

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, specialty)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def _calculateSalary(self):
        return self.__hourly_rate * self.__hours_worked

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self.__hourly_rate = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self.__hours_worked = value

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthly_salary):
        super().__init__(name, phone, birthday, email, specialty)
        self.__monthly_salary = monthly_salary

    def _calculateSalary(self):
        return self.__monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self.__monthly_salary = value
