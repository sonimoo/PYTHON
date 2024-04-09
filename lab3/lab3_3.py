import functions as func

shopping_list = []

while True:
    print("\nМеню:")
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в список")
    print("3. Удалить товар")
    print("4. Выход")

    choice = input("Выберите опцию (1-4): ")

    if choice == '1':
        func.display_list(shopping_list)
    elif choice == '2':
        item = input("Введите название товара, который хотите добавить: ")
        func.add_item(shopping_list, item)
    elif choice == '3':
        print("\nМеню удаления:")
        print("1. Удалить товар по названию")
        print("2. Удалить товар по порядковому номеру")
        delete_choice = input("Выберите опцию удаления (1-2): ")

        if delete_choice == '1':
            item = input("Введите название товара, который хотите удалить: ")
            func.delete_item_by_name(shopping_list, item)
        elif delete_choice == '2':
            index = int(input("Введите порядковый номер товара, который хотите удалить: "))
            func.delete_item_by_index(shopping_list, index)
        else:
            print("Некорректный выбор удаления. Попробуйте снова.")
    elif choice == '4':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")



