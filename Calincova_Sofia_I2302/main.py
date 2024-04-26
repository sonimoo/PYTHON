import functions

while True:
    print("Меню:")
    print("1) Записать данные об успеваемости ученика в файл")
    print("2) Вывести среднюю арифметическую оценку по всему классу")
    print("3) Вывести список учеников с оценками меньше 5")
    print("4) Вывести список учеников, имеющие оценки больше 8")
    print("5) Выход")

    choice = input("Выберите опцию: ")

    if choice == '1':
        functions.input_data()
    elif choice == '2':
        functions.calculate_grade()
    elif choice == '3':
        functions.grades_below_5()
    elif choice == '4':
        functions.grades_above_8()
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод, попробуйте еще раз.")
