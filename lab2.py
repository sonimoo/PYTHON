#1
#b
arr1 = [5.3, 2, 4.5, "33", 10]
print (arr1[0])
print (arr1[2])

arr1[3] = 33
print (arr1)

print(arr1[1:3])

 #функции
print(len(arr1))
print(sorted(arr1))
print(min(arr1))

#методы

arr1.append(4)
print(arr1)

arr1.remove(10)
print(arr1)

index = arr1.index(2)
print(index)

count = arr1.count(33)
print(count)

#c

tuple1 = (5.3, 2, 4.5, 33, 10)
print(type(tuple1))

print(tuple1[0])
print(tuple1[-1])

print(tuple1[:3])

#функции
tupleList = tuple(arr1)
print(tupleList)
print(type(tupleList))

print(len(tuple1))

print(max(tuple1))

#d
set1 = {1, 3, 2, 5, 2, 6, 2}
print(set1)

set1.add(8)
print(set1)

set1.discard(6)
print(set1)

print(len(set1))

#e

dict1 = {'name':'Sofia','age':20, 'homeTown':'Tvarditsa'}
dict2 = {1:"a", 2:"b", 3:"c"}
print(dict1['name'])
print(dict2[3])

#функции

print(len(dict1))
print(dict2.values()) #Метод values() - возвращает объект, который отображает список всех значений в словаре



keys = dict1.keys()
print(keys)   # Метод для получения значения по ключу. Если ключ отсутствует, возвращает значение по умолчанию.

value = dict1.get ('age')
print(value)

dict2.clear()
print(dict2)

setList = list(set1)
print(setList)
print(type(setList))


#2

list2 = [200, 10, 6]
list3 = ["book", "pen", "apple"]

order = (" {} costs {}")
print(order.format(list3[0],list2[0]))
print(order.format(list3[1],list2[1]))
print(order.format(list3[2],list2[2]))
#Метод format() принимает переданные ему аргументы, форматирует их и помещает их в строку, где находит заполнители {}.


yourAge = input("Введите ваш возраст:")
futureAge = int(yourAge)+5
print("Через 5 лет вам будет " + str(futureAge))

text1 = "Good night"
word1 = "Good"
if word1 in text1:
    print(text1)



