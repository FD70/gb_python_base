# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ["abc", 1, 3.1415, False, None, [3,4], (5,6), {"1": 1}]

for i in my_list:
    print(type(i))
