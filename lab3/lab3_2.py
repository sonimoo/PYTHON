#2

number = int(input("Введите число: "))

if number > 0:
    print("Ваше число положительное.")
elif number < 0:
    print ("Ваше число отрицательное.")
else:
    print("Ваше число равно нулю.")


# b
fruits = ["apple", "banana", "orange", "banana", "kiwi", "banana", "grape"]
fruit = "banana"

# Инициализация счетчика
count1 = 0

# Индекс для цикла while
index = 0

while index < len(fruits):
    if fruits[index] == fruit:
        count1 += 1
    index += 1

print(fruit + " встречается " + str(count1) + " раз(а) в списке.")



age_dict = {'Alisa': 15, 'Vika': 19, 'Ivan': 12, 'Elena': 25, 'Eva': 15, 'Matvei': 18}
age = 15

# Инициализация счетчика
count2 = 0

for key, value in age_dict.items():
    if value == age:
        count2 += 1

print(str(age)+ " встречается " + str(count2) + " раз(а) в списке.")

#c

numberSquared = lambda x: x ** 2

number = int(input("Введите число: "))
print(numberSquared(number))

