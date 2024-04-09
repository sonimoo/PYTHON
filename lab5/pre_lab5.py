import re

try:
    input_number = input("Введите номер телефона: ")

    pattern = '^(\\+373|00373)?([0-9]{8})$'

    if not re.match(pattern, input_number):
        raise ValueError("Этот номер не валиден :/")

except ValueError as err:
    print("Ошибка: ", err)

else:
    print('Этот номер валиден ')
