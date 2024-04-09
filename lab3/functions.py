()
def display_list(shopping_list):
    if shopping_list:
        print("\nСписок покупок:")
        count = 1
        for item in shopping_list:
            print("{}. {}".format(count, item))
            count += 1
    else:
        print("Список покупок пуст.")

def add_item(shopping_list, item):
    shopping_list.append(item)
    print("{} успешно добавлен в список покупок.".format(item))

def delete_item_by_name(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print("{} успешно удален из списка покупок.".format(item))
    else:
        print("Товар с названием '{}' не найден в списке.".format(item))

def delete_item_by_index(shopping_list, index):
    if 0 < index <= len(shopping_list):
        deleted_item = shopping_list.pop(index - 1)
        print("Товар '{}' успешно удален из списка покупок.".format(deleted_item))
    else:
        print("Некорректный порядковый номер товара.")
