#from classes import Employee, HourlyEmployee, SalaryEmployee
from classes2 import Employee, HourlyEmployee, SalaryEmployee

def create_employee(cls, employee_type):
    print(f"\nСоздание сотрудника типа {employee_type}:")
    name = input("Введите имя: ")
    phone = input("Введите телефон (+373xxxxxxxx): ")
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    email = input("Введите email: ")
    specialty = input("Введите специальность: ")
    if cls is HourlyEmployee:
        hourly_rate = float(input("Введите почасовую ставку: "))
        hours_worked = float(input("Введите количество отработанных часов: "))
        return cls(name, phone, birthday, email, specialty, hourly_rate, hours_worked)
    elif cls is SalaryEmployee:
        monthly_salary = float(input("Введите месячную зарплату: "))
        return cls(name, phone, birthday, email, specialty, monthly_salary)
    else:
        return cls(name, phone, birthday, email, specialty)

def input_employees():
    # Ввод данных для обычного сотрудника
    general_employee = create_employee(Employee, "обычного")

    # Ввод данных для сотрудника с почасовой оплатой
    hourly_employee = create_employee(HourlyEmployee, "почасового")

    # Ввод данных для сотрудника с фиксированной оплатой
    salary_employee = create_employee(SalaryEmployee, "с фиксированной оплатой")

    return general_employee, hourly_employee, salary_employee

def display_salaries(general_employee, hourly_employee, salary_employee):
    print("\nЗарплаты всех сотрудников:")
    print(f"{general_employee.name}: {general_employee._calculateSalary()}")
    print(f"{hourly_employee.name}: {hourly_employee._calculateSalary()}")
    print(f"{salary_employee.name}: {salary_employee._calculateSalary()}")

# Сбор данных о всех сотрудниках
general_employee, hourly_employee, salary_employee = input_employees()

# Отображение зарплат всех сотрудников
display_salaries(general_employee, hourly_employee, salary_employee)
