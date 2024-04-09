import functions

while True:
    print("\nМеню:")
    print("1. Добавить проданный товар")
    print("2. Отобразить список проданных товаров")
    print("3. Добавить новый товар")
    print("4. Изменить детали продукта")
    print("5. Удалить товар")
    print("6. Вывести общую стоимость проданных товаров")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        functions.add_sold_product()
    elif choice == "2":
        functions.display_list()
    elif choice == "3":
        functions.add_new_product()
    elif choice == "4":
        functions.change_details()
    elif choice == "5":
        functions.delete_product()
    elif choice == "6":
        functions.total_sum()
    elif choice == "7":
        print("Выход из программы")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
