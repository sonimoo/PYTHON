import functions as func

while True:
    print("\nМеню:")
    print("1. Ввод двнных в файл")
    print("2. Просмотр данных о детях сотрудников")
    print("3. Поиск и вывод списка бездетных сотрудников")
    print("4. Выход")

    choice = input("Выберите опцию (1-4): ")

    if choice == '1':
        func.input_data()
    elif choice == '2':
        func.output_data()
    elif choice == '3':
        func.no_kids()
    elif choice == '4':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
