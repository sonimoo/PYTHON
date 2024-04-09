productList = []


def add_sold_product():
    name = input("Введите название продукта: ")
    price = input("Введите цену продукта: ")
    if price.isdigit():
        quantity = input("Введите количество проданного товара: ")
        if quantity.isdigit():
            productList.append({"name": name, "price": price, "quantity": quantity})
            print("Продукт успешно добавлен в список")
        else:
            print("Количество, введенное Вами должно быть целым числом!!!")
    else:
        print("Цена, введенная вами должно быть целым числом!!!")


def display_list():
    for product in productList:
        print("Продукт: {} - Цена: {} - Количество: {}".format(product['name'], product['price'], product['quantity']))


def add_new_product():

    name = input("Введите название продукта: ")

    if any(product['name'].upper() == name.upper() for product in productList):
        print("Этот продукт уже есть в списке")
    else:
        price = input("Введите цену продукта: ")
        if price.isdigit():
            quantity = input("Введите количество проданного товара: ")
            if quantity.isdigit():
                productList.append({"name": name, "price": price, "quantity": quantity})
                print("Продукт успешно добавлен в список")
            else:
                print("Количество, введенное Вами должно быть целым числом!!!")
        else:
            print("Цена, введенная вами должно быть целым числом!!!")


def change_details():
    name = input("Введите название продукта для изменения: ")

    for product in productList:
        if product['name'] == name:
            print("Что вы хотите изменить?")
            print("1. Цена")
            print("2. Количество")
            print("3. Оба поля")

            choice = input("Выберите опцию (1, 2 или 3): ")

            if choice == "1":
                new_price = input("Введите новую цену: ")
                if new_price.isdigit():
                    product['price'] = new_price
                else:
                    print("Цена должна быть целым числом.")
                print("Детали об этом товаре изменены.")
            elif choice == "2":
                new_quantity = input("Введите новое количество: ")
                if new_quantity.isdigit():
                    product['quantity'] = new_quantity
                else:
                    print("Количество должно быть целым числом.")
                print("Детали об этом товаре изменены.")
            elif choice == "3":
                new_price = input("Введите новую цену: ")
                new_quantity = input("Введите новое количество: ")
                if new_price.isdigit() and new_quantity.isdigit():
                    product['price'] = new_price
                    product['quantity'] = new_quantity
                    print("Детали об этом товаре изменены.")
                else:
                    print("Цена и количество должны быть целыми числами.")
            else:
                print("Некорректный выбор.")
            break
    else:
        print("Продукт '{}' не найден в списке.".format(name))


def delete_product():
    name = input("Введите название продукта для удаления: ")

    for product in productList:
        if product['name'] == name:
            productList.remove(product)
            print("Продукт '{}' успешно удален.".format(name))
            break
    else:
        print("Продукт '{}' не найден.".format(name))


def total_sum():
    total_s = 0
    for product in productList:
        total_s += int(product['price']) * int(product['quantity'])
    print("Общая стоимость проданных товаров из списка: {} ".format(total_s))
