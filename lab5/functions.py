import re

'''name_pattern = '^[a-zA-Z]+(-[a-zA-Z]+)?{1,19}$'''
'''name_pattern = '^[A-zА-я]{1,10}(-[A-zА-я]{1,10})?$'''
name_pattern = '^[A-zА-я]+(-[A-zА-я]+)?$'
surname_pattern = '^[A-zА-я]+(-[A-zА-я]+)?$'
'''department_pattern = '^[A-zА-я0-9]+( [A-zА-я0-9]+)?$'''
department_pattern = '^[A-zА-я0-9]+(?: [A-zА-я0-9]+)?$'
kids_pattern = '^([0-9]|1[0-9])$'


def input_data():
    while True:
        name = input("Введите имя сотрудника: ")
        surname = input("Введите фамилию сотрудника: ")
        department = input("Введите отдел, в котором работает сотрудник: ")
        kids_number = input("Введите количество детей до 18 лет: ")

        match_it1 = re.match(name_pattern, name)
        match_it2 = re.match(surname_pattern, surname)
        match_it3 = re.match(department_pattern, department)
        match_it4 = re.match(kids_pattern, kids_number)

        if match_it1 and match_it2 and match_it3 and match_it4:
            data = f"{name}\t{surname}\t{department}\t{kids_number}"

            with open("date.txt", mode='a', encoding='utf-8') as f:
                f.write(data + "\n")
            print("Данные успешно сохранены в файл data.txt.")
            break
        else:
            print("Ошибка ввода. Повторите ввод.")
            continue


def output_data():
    with open("date.txt", mode="r", encoding='utf-8') as f:
        my_data = f.readlines()
        counter = 0
        print("Список сотрудников:")
        for line in my_data:
            word = line.split()

            counter += int(word[-1])
            print(word)
    print(f"Всего детей у сотрудников -> {counter}")


def no_kids():
    with open("date.txt", mode="r", encoding='utf-8') as f:
        my_data = f.readlines()
        print("Список сотрудников без детей:")
        for line in my_data:
            word = line.split()

            if int(word[-1]) == 0:
                print(word[0], word[1])
                no_kids_found = True

        if not no_kids_found:
            print("У всех сотрудников есть дети")
