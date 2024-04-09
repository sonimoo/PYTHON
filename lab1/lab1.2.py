txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip()) #Метод strip() удаляет любые пробелы в начале или в конце текста

txt = "More results from text..."
print(txt.split()) #Метод split() разбивает строку на подстроки, если находит экземпляры
# разделителя в строке. Подстроки сохраняются как элементы списка

age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age)) #Метод format() принимает переданные ему аргументы, форматирует их
# и помещает их в строку, где находит заполнители {}.
# Можно использовать метод format() для вставки чисел в строки

