print('Давайте посчитаем Ваш "идеальный" вес')

ideal = 0

height = input("Введите Ваш рост в см: ")
age = input("Введите Ваш возраст: ")
gender = input("Введите Ваш пол (М, если Вы мужчина, Ж, если Вы женщина): ")

if age.isdigit() and height.isdigit():
    if gender.upper() == "М":
        ideal = float(height) - 100 - (float(height) - 150) / 4 + (int(age) - 20) / 4
        print("Ваш идеальный вес в кг = ", ideal)

    elif gender.upper() == "Ж":
        ideal = float(height) - 100 - (float(height) - 150) / 2.5 + (int(age) - 20) / 6
        print("Ваш идеальный вес в кг = ", ideal)

    else:
        print("Вы неправильно указали пол!!!")

else:
    print("Возраст или вес, который Вы ввели содержит НЕ только цифры")

weight = float(input("Введите свой текущий вес: "))

if weight < ideal:
    print("Вам следует набрать вес")
elif weight > ideal:
    print("Вам следует снизить вес")
else:
    print("У Вас идеальный вес")
