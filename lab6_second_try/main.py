#from classes2 import HourlyEmployee, SalaryEmployee, Employee
from classes import HourlyEmployee, SalaryEmployee, Employee


def input_employee(target_class):
    print(f"\nНачинаем ввод данных для {target_class.__name__}.")
    name = input("Введите имя сотрудника: ")
    phone = input("Введите телефон сотрудника (+373xxxxxxxx): ")
    birthday = input("Введите дату рождения (дд.мм.гггг): ")
    email = input("Введите email сотрудника: ")
    position = input("Введите должность сотрудника: ")

    if target_class == HourlyEmployee:
        hourly_rate = float(input("Введите почасовую ставку: "))
        hours_worked = int(input("Введите количество отработанных часов: "))
        employee = target_class(name, phone, birthday, email, position, hourly_rate, hours_worked)
    elif target_class == SalaryEmployee:
        monthly_salary = float(input("Введите месячную зарплату: "))
        employee = target_class(name, phone, birthday, email, position, monthly_salary)
    else:
        employee = target_class(name, phone, birthday, email, position)

    if all([employee.name, employee.phone, employee.birthday, employee.email, employee.position]):
        return employee
    else:
        print("Одно или несколько введённых значений некорректны. Попробуйте заново.")
        return input_employee(target_class)


# Создаем по одному (ХОТЯ ТАМ НАДО ПО ДВА) объекту каждого класса
general_employee = input_employee(Employee)
hourly_employee = input_employee(HourlyEmployee)
salary_employee = input_employee(SalaryEmployee)

# Выводим информацию о зарплатах и возрасте
employees = [general_employee, hourly_employee, salary_employee]
for emp in employees:
    print(f"\nИнформация о сотруднике {emp.name}:")
    print(f"Возраст: {emp.calculate_age()}")
    if isinstance(emp, (HourlyEmployee, SalaryEmployee)):
        print(f"Зарплата: {emp._calculate_salary()} ДЕНЕГ.")